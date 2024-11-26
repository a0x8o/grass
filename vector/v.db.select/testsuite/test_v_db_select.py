"""
Name:      vdbselect_test
Purpose:   v.db.select decimation test

Author:    Luca Delucchi
Copyright: (C) 2015 by Luca Delucchi and the GRASS Development Team
Licence:   This program is free software under the GNU General Public
           License (>=v2). Read the file COPYING that comes with GRASS
           for details.
"""

import os
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.gunittest.gmodules import SimpleModule

out_group = """CZab
CZam
CZba
CZbb
CZbf
CZbg
CZbl
CZc
CZfg
CZfv
CZfv1
CZfv2
CZg
CZgms
CZig
CZiv
CZlg
CZma
CZma1
CZma2
CZmd
CZmd1
CZmd2
CZmd3
CZmg
CZms
CZmv
CZmv1
CZpg
CZph
CZq
CZtp
CZv
CZve
CZy
Ccl
Ccu
Chg
Cr
Cs
DOg
DOgb
DSc
DSg
DSs
Dqd
Dsc
Jd
Kb
Kc
Km
Kp
Mc
OCg
OCgm
Org
PPg
PPgb
PPmg
PzZg
PzZm
PzZq
PzZu
Qp
SOgg
Sg
TRc
TRcc
TRcp
TRcs
TRd
TRdc
TRdp
TRds
Tec
Tecs
Tob
Tor
Tp
Tpa
Tpy
Tpyw
Tt
Ybam
Ybgg
Ybrg
Yg
Ygg
Ymam
Ymg
Ytg
ZYbA
ZYba
ZYbn
Za
Zaba
Zabg
Zabs
Zata
Zatb
Zatm
Zats
Zatw
Zb
Zbg
Zbt
Zch
Zchs
Zco
Zd
Zf
Zg
Zgma
Zgmf
Zgmg
Zgms
Zgmu
Zgmw
Zgs
Zhha
Zlm
Zm
Zman
Zmb
Zmf
Zml
Znt
Zrb
Zs
Zsl
Zsp
Zsr
Zss
Zsw
Zwc
Zwe
bz
"""

out_where = """1076|366545504|324050.96875|1077|1076|Zwe|366545512.376|324050.97237
1123|1288.555298|254.393951|1124|1123|Zwe|1288.546525|254.393964
1290|63600420|109186.835938|1291|1290|Zwe|63600422.4739|109186.832069
"""

out_sep = """1076,366545504,324050.96875,1077,1076,Zwe,366545512.376,324050.97237
1123,1288.555298,254.393951,1124,1123,Zwe,1288.546525,254.393964
1290,63600420,109186.835938,1291,1290,Zwe,63600422.4739,109186.832069
"""

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
out_json = """{"records":[
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
out_json = """{"records":[
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 136ff55649 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 785f930004 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7df6db66ca (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 53af05a205 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f90ac90130 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e9ac05e439 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3f2d73dc8e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 333b795855 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7828caa6b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5208988082 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4ee1687e37 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0d464f36be (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
out_json = """{"records":[
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 136ff55649 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 785f930004 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7df6db66ca (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 53af05a205 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f90ac90130 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e9ac05e439 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3f2d73dc8e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 333b795855 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7828caa6b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5208988082 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4ee1687e37 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0d464f36be (WMS: replace broken URLs with alternative WMS (#1635))
out_json = """\
{"info":
{"columns":[
{"name":"cat","sql_type":"INTEGER","is_number":true},
{"name":"onemap_pro","sql_type":"DOUBLE PRECISION","is_number":true},
{"name":"PERIMETER","sql_type":"DOUBLE PRECISION","is_number":true},
{"name":"GEOL250_","sql_type":"INTEGER","is_number":true},
{"name":"GEOL250_ID","sql_type":"INTEGER","is_number":true},
{"name":"GEO_NAME","sql_type":"CHARACTER","is_number":false},
{"name":"SHAPE_area","sql_type":"DOUBLE PRECISION","is_number":true},
{"name":"SHAPE_len","sql_type":"DOUBLE PRECISION","is_number":true}
]},
"records":[
=======
out_json = """{"records":[
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 136ff55649 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 785f930004 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7df6db66ca (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 53af05a205 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f90ac90130 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e9ac05e439 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3f2d73dc8e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 333b795855 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7828caa6b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5208988082 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4ee1687e37 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0d464f36be (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
out_json = """{"records":[
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 136ff55649 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 136ff55649 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 8d63674c88 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 785f930004 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
out_json = """{"records":[
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1f29aef40 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7df6db66ca (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8cdf2763b4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 53af05a205 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8b5db77cc8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f90ac90130 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 897ec22b89 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e9ac05e439 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 84365c60c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3f2d73dc8e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7a02ec5519 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 333b795855 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 179aa8f0a6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7828caa6b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bd05168e52 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5208988082 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 515877a709 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 4ee1687e37 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aac8b57eb9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0d464f36be (WMS: replace broken URLs with alternative WMS (#1635))
{"cat":1,"onemap_pro":963738.75,"PERIMETER":4083.97998,"GEOL250_":2,"GEOL250_ID":1,"GEO_NAME":"Zml","SHAPE_area":963738.608571,"SHAPE_len":4083.979839},
{"cat":2,"onemap_pro":22189124,"PERIMETER":26628.261719,"GEOL250_":3,"GEOL250_ID":2,"GEO_NAME":"Zmf","SHAPE_area":22189123.2296,"SHAPE_len":26628.261112},
{"cat":3,"onemap_pro":579286.875,"PERIMETER":3335.55835,"GEOL250_":4,"GEOL250_ID":3,"GEO_NAME":"Zml","SHAPE_area":579286.829631,"SHAPE_len":3335.557182},
{"cat":4,"onemap_pro":20225526,"PERIMETER":33253,"GEOL250_":5,"GEOL250_ID":4,"GEO_NAME":"Zml","SHAPE_area":20225526.6368,"SHAPE_len":33253.000508},
{"cat":5,"onemap_pro":450650720,"PERIMETER":181803.765625,"GEOL250_":6,"GEOL250_ID":5,"GEO_NAME":"Ybgg","SHAPE_area":450650731.029,"SHAPE_len":181803.776199},
{"cat":6,"onemap_pro":6386874.5,"PERIMETER":17978.429688,"GEOL250_":7,"GEOL250_ID":6,"GEO_NAME":"Zml","SHAPE_area":6386875.00182,"SHAPE_len":17978.430892},
{"cat":7,"onemap_pro":969311.1875,"PERIMETER":4096.096191,"GEOL250_":8,"GEOL250_ID":7,"GEO_NAME":"Ybgg","SHAPE_area":969311.720138,"SHAPE_len":4096.098584},
{"cat":8,"onemap_pro":537840.625,"PERIMETER":3213.40625,"GEOL250_":9,"GEOL250_ID":8,"GEO_NAME":"Zmf","SHAPE_area":537840.953797,"SHAPE_len":3213.407197},
{"cat":9,"onemap_pro":3389078.25,"PERIMETER":16346.604492,"GEOL250_":10,"GEOL250_ID":9,"GEO_NAME":"Zml","SHAPE_area":3389077.17888,"SHAPE_len":16346.604884},
{"cat":10,"onemap_pro":906132.375,"PERIMETER":4319.162109,"GEOL250_":11,"GEOL250_ID":10,"GEO_NAME":"Zml","SHAPE_area":906132.945012,"SHAPE_len":4319.163379}
]}"""


class SelectTest(TestCase):
    """Test case for v.db.select"""

    outfile = "select.csv"
    invect = "geology"
    col = "GEO_NAME"
    val = "Zwe"
    cat = 10

    def testRun(self):
        """Module runs with minimal parameters and give output."""
        sel = SimpleModule(
            "v.db.select",
            map=self.invect,
        )
        sel.run()
        self.assertTrue(sel.outputs.stdout, msg="There should be some output")

    def testFileExists(self):
        """This function checks if the output file is written correctly"""
        self.runModule("v.db.select", map=self.invect, file=self.outfile)
        self.assertFileExists(self.outfile)
        if os.path.isfile(self.outfile):
            os.remove(self.outfile)

    def testGroup(self):
        """Testing v.db.select with group option"""
        sel = SimpleModule(
            "v.db.select", flags="c", map=self.invect, columns=self.col, group=self.col
        )
        sel.run()
        self.assertLooksLike(reference=out_group, actual=sel.outputs.stdout)

    def testWhere(self):
        """Testing v.db.select with where option"""
        sel = SimpleModule(
            "v.db.select",
            flags="c",
            map=self.invect,
            where="{col}='{val}'".format(col=self.col, val=self.val),
        )
        sel.run()
        self.assertLooksLike(reference=out_where, actual=sel.outputs.stdout)

    def testSeparator(self):
        sel = SimpleModule(
            "v.db.select",
            flags="c",
            map=self.invect,
            where="{col}='{val}'".format(col=self.col, val=self.val),
            separator="comma",
        )
        sel.run()
        self.assertLooksLike(reference=out_sep, actual=sel.outputs.stdout)

    def testComma(self):
        sel = SimpleModule(
            "v.db.select",
            flags="c",
            map=self.invect,
            where="{col}='{val}'".format(col=self.col, val=self.val),
            separator=",",
        )
        sel.run()
        self.assertLooksLike(reference=out_sep, actual=sel.outputs.stdout)

    def testJSON(self):
        """Test that JSON can be decoded and formatted exactly as expected"""
        import json

        sel = SimpleModule(
            "v.db.select",
            format="json",
            map=self.invect,
            where="cat<={cat}".format(cat=self.cat),
        )
        sel.run()

        try:
            json.loads(sel.outputs.stdout)
        except ValueError:
            self.fail(msg="No JSON object could be decoded:\n" + sel.outputs.stdout)

        self.assertLooksLike(reference=out_json, actual=sel.outputs.stdout)


if __name__ == "__main__":
    test()
