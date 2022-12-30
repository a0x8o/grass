#!/bin/sh
# This is a test to list raster maps of a space time raster dataset

# We need to set a specific region in the
# @preprocess step of this test. We generate
# raster maps with r.mapcalc and create a space time raster datasets
# The region setting should work for UTM and LL test locations
g.region s=0 n=80 w=0 e=120 b=0 t=50 res=10 res3=10 -p3

export GRASS_OVERWRITE=1

# Generate data
r.mapcalc expr="prec_1 = rand(0, 550)" -s
r.mapcalc expr="prec_2 = rand(0, 450)" -s
r.mapcalc expr="prec_3 = rand(0, 320)" -s
r.mapcalc expr="prec_4 = rand(0, 510)" -s
r.mapcalc expr="prec_5 = rand(0, 300)" -s
r.mapcalc expr="prec_6 = rand(0, 650)" -s

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
n1=`g.tempfile pid=1 -d`
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
n1=`g.tempfile pid=1 -d`
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
>>>>>>> osgeo-main
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
n1=`g.tempfile pid=1 -d`
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
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
n1=`g.tempfile pid=1 -d` 
=======
n1=`g.tempfile pid=1 -d`
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
n1=`g.tempfile pid=1 -d`
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
n1=`g.tempfile pid=1 -d`
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
n1=`g.tempfile pid=1 -d`
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
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
n1=`g.tempfile pid=1 -d`
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
n1=`g.tempfile pid=1 -d`
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
n1=`g.tempfile pid=1 -d` 
=======
n1=`g.tempfile pid=1 -d`
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
n1=`g.tempfile pid=1 -d` 
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
n2=`g.tempfile pid=2 -d`
n3=`g.tempfile pid=3 -d`
n4=`g.tempfile pid=4 -d`
n5=`g.tempfile pid=5 -d`

cat > "${n1}" << EOF
prec_1
prec_2
prec_3
prec_4
prec_5
prec_6
EOF

cat > "${n2}" << EOF
prec_1|2001-01-01
prec_2|2001-03-01
prec_3|2001-04-01
prec_4|2001-05-01
prec_5|2001-08-01
prec_6|2001-09-01
EOF

cat > "${n3}" << EOF
prec_1|2001-01-01|2001-04-01
prec_2|2001-05-01|2001-07-01
prec_3|2001-08-01|2001-10-01
prec_4|2001-11-01|2002-01-01
prec_5|2002-02-01|2002-04-01
prec_6|2002-05-01|2002-07-01
EOF

cat > "${n4}" << EOF
prec_1|2001-01-01|2001-07-01
prec_2|2001-02-01|2001-04-01
prec_3|2001-03-01|2001-04-01
prec_4|2001-04-01|2001-06-01
prec_5|2001-05-01|2001-06-01
prec_6|2001-06-01|2001-07-01
EOF

cat > "${n5}" << EOF
prec_1|2001-01-01|2001-03-11
prec_2|2001-02-01|2001-04-01
prec_3|2001-03-01|2001-06-02
prec_4|2001-04-01|2001-04-01
prec_5|2001-05-01|2001-05-01
prec_6|2001-06-01|2001-07-01
EOF

t.create type=strds temporaltype=absolute output=precip_abs0 title="A test with input files" descr="A test with input files"

# The @test
t.register type=raster -i input=precip_abs0 file="${n1}" start="2001-01-01" increment="1 month"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  input=precip_abs0
t.rast.list  separator=" | " method=cols      input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="2 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="1 day"

t.register type=raster input=precip_abs0 file="${n1}" start="2001-01-01" increment="1 month"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  input=precip_abs0
t.rast.list  separator=" | " method=cols      input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="2 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="6 days"

t.register type=raster input=precip_abs0 file="${n2}"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  input=precip_abs0
t.rast.list  separator=" | " method=cols      input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="2 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="6 days"

t.register type=raster input=precip_abs0 file="${n3}"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="2 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="6 days"

t.register type=raster input=precip_abs0 file="${n4}"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="2 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="6 days"

t.register type=raster input=precip_abs0 file="${n5}"
t.rast.list  separator=" | " method=comma     input=precip_abs0
t.rast.list  input=precip_abs0
t.rast.list  separator=" | " method=cols      input=precip_abs0
t.rast.list  separator=" | " method=delta     input=precip_abs0
t.rast.list  separator=" | " method=deltagaps input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="8 months"
t.rast.list  separator=" | " method=gran      input=precip_abs0 gran="13 days"

t.unregister type=raster maps=prec_1,prec_2,prec_3,prec_4,prec_5,prec_6
t.remove type=strds input=precip_abs0
