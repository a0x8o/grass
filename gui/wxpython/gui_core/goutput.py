"""
@package gui_core.goutput

@brief Command output widgets

Classes:
 - goutput::GConsoleWindow
 - goutput::GStc
 - goutput::GConsoleFrame

(C) 2007-2012 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton (Arizona State University)
@author Martin Landa <landa.martin gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com>  (refactoring)
@author Anna Kratochvilova <kratochanna gmail.com> (refactoring)
"""

import textwrap
from string import digits

import wx
from wx import stc

from grass.pydispatch.signal import Signal

# needed just for testing
if __name__ == "__main__":
    from grass.script.setup import set_gui_path

    set_gui_path()

from core.gcmd import GError
from core.gconsole import (
    GConsole,
    EVT_CMD_OUTPUT,
    EVT_CMD_PROGRESS,
    EVT_CMD_RUN,
    EVT_CMD_DONE,
    Notification,
)
from core.globalvar import CheckWxVersion, wxPythonPhoenix
from gui_core.prompt import GPromptSTC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
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
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
from gui_core.wrap import Button, ClearButton, StaticText
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
from gui_core.wrap import Button, ClearButton, StaticText, StaticBox
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
from core.settings import UserSettings


GC_EMPTY = 0
GC_PROMPT = 1


class GConsoleWindow(wx.SplitterWindow):
    """Create and manage output console for commands run by GUI."""

    def __init__(
        self,
        parent,
        giface,
        gconsole,
        menuModel=None,
        margin=False,
        style=wx.TAB_TRAVERSAL | wx.FULL_REPAINT_ON_RESIZE,
        gcstyle=GC_EMPTY,
        **kwargs,
    ):
        """
        :param parent: gui parent
        :param gconsole: console logic
        :param menuModel: tree model of modules (from menu)
        :param margin: use margin in output pane (GStc)
        :param style: wx.SplitterWindow style
        :param gcstyle: GConsole style
                        (GC_EMPTY, GC_PROMPT to show command prompt)
        """
        wx.SplitterWindow.__init__(self, parent, id=wx.ID_ANY, style=style, **kwargs)
        self.SetName("GConsole")

        self.panelOutput = wx.Panel(parent=self, id=wx.ID_ANY)
        self.panelProgress = wx.Panel(
            parent=self.panelOutput, id=wx.ID_ANY, name="progressPanel"
        )
        self.panelPrompt = wx.Panel(parent=self, id=wx.ID_ANY)
        # initialize variables
        self.parent = parent  # GMFrame | CmdPanel | ?
        self.giface = giface
        self._gconsole = gconsole
        self._menuModel = menuModel

        self._gcstyle = gcstyle
        self.lineWidth = 80

        # signal which requests showing of a notification
        self.showNotification = Signal("GConsoleWindow.showNotification")
        # signal emitted when text appears in the console
        # parameter 'notification' suggests form of notification (according to
        # core.giface.Notification)
        self.contentChanged = Signal("GConsoleWindow.contentChanged")

        # progress bar
        self.progressbar = wx.Gauge(
            parent=self.panelProgress,
            id=wx.ID_ANY,
            range=100,
            pos=(110, 50),
            size=(-1, 25),
            style=wx.GA_HORIZONTAL,
        )
        self._gconsole.Bind(EVT_CMD_PROGRESS, self.OnCmdProgress)
        self._gconsole.Bind(EVT_CMD_OUTPUT, self.OnCmdOutput)
        self._gconsole.Bind(EVT_CMD_RUN, self.OnCmdRun)
        self._gconsole.Bind(EVT_CMD_DONE, self.OnCmdDone)

        self._gconsole.writeLog.connect(self.WriteLog)
        self._gconsole.writeCmdLog.connect(self.WriteCmdLog)
        self._gconsole.writeWarning.connect(self.WriteWarning)
        self._gconsole.writeError.connect(self.WriteError)

        # text control for command output
        self.cmdOutput = GStc(
            parent=self.panelOutput, id=wx.ID_ANY, margin=margin, wrap=None
        )

        # command prompt
        # move to the if below
        # search depends on cmd prompt
        self.cmdPrompt = GPromptSTC(
            parent=self, giface=giface, menuModel=self._menuModel
        )
        self.cmdPrompt.promptRunCmd.connect(
            lambda cmd: self._gconsole.RunCmd(command=cmd)
        )
        self.cmdPrompt.showNotification.connect(self.showNotification)

        if not self._gcstyle & GC_PROMPT:
            self.cmdPrompt.Hide()

        # buttons
        self.btnClear = ClearButton(parent=self.panelPrompt)
        self.btnClear.SetToolTip(_("Clear prompt and output window"))
        self.btnOutputSave = Button(parent=self.panelPrompt, id=wx.ID_SAVE)
        self.btnOutputSave.SetToolTip(_("Save output to a file"))
        self.btnCmdAbort = Button(parent=self.panelProgress, id=wx.ID_STOP)
        self.btnCmdAbort.SetToolTip(_("Abort running command"))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
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
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))

        self.btnClear.Bind(wx.EVT_BUTTON, self.OnClear)
        self.btnOutputSave.Bind(wx.EVT_BUTTON, self.OnOutputSave)
        self.btnCmdAbort.Bind(wx.EVT_BUTTON, self._gconsole.OnCmdAbort)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> osgeo-main
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
        self.btnCmdExportHistory = Button(parent=self.panelOutput, id=wx.ID_ANY)
        self.btnCmdExportHistory.SetLabel(_("&Export history"))
        self.btnCmdExportHistory.SetToolTip(
            _("Export history of executed commands to a file")
        )

        if not self._gcstyle & GC_PROMPT:
            self.btnCmdClear.Hide()
            self.btnCmdExportHistory.Hide()

        self.btnCmdClear.Bind(wx.EVT_BUTTON, self.cmdPrompt.OnCmdErase)
        self.btnOutputClear.Bind(wx.EVT_BUTTON, self.OnOutputClear)
        self.btnOutputSave.Bind(wx.EVT_BUTTON, self.OnOutputSave)
        self.btnCmdAbort.Bind(wx.EVT_BUTTON, self._gconsole.OnCmdAbort)
        self.btnCmdExportHistory.Bind(wx.EVT_BUTTON, self.OnCmdExportHistory)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))

        self._layout()

    def _layout(self):
        """Do layout"""
        self.outputSizer = wx.BoxSizer(wx.VERTICAL)
        progressSizer = wx.BoxSizer(wx.HORIZONTAL)

        if self._gcstyle & GC_PROMPT:
            promptSizer = wx.BoxSizer(wx.VERTICAL)
            promptSizer.Add(
                self.cmdPrompt,
                proportion=1,
                flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP,
                border=3,
            )
            helpText = StaticText(
                self.panelPrompt,
                id=wx.ID_ANY,
                label="Press Tab to display command help, Ctrl+Space to autocomplete",
            )
            helpText.SetForegroundColour(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT)
            )
            promptSizer.Add(helpText, proportion=0, flag=wx.EXPAND | wx.LEFT, border=5)

            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.AddStretchSpacer()
            btnSizer.Add(
                self.btnOutputSave,
                proportion=0,
                flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
                border=5,
            )
            btnSizer.Add(self.btnClear, proportion=0, flag=wx.EXPAND, border=5)
            promptSizer.Add(btnSizer, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)

        self.outputSizer.Add(
            self.cmdOutput, proportion=1, flag=wx.EXPAND | wx.ALL, border=3
        )

<<<<<<< HEAD
=======
        outBtnSizer.Add(
            self.btnOutputClear,
            proportion=proportion,
            flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT | wx.BOTTOM,
            border=5,
        )

        outBtnSizer.Add(
            self.btnOutputSave,
            proportion=proportion,
            flag=wx.RIGHT | wx.BOTTOM,
            border=5,
        )

        cmdBtnSizer.Add(
            self.btnCmdExportHistory,
            proportion=1,
            flag=wx.ALIGN_CENTER
            | wx.ALIGN_CENTER_VERTICAL
            | wx.LEFT
            | wx.RIGHT
            | wx.BOTTOM,
            border=5,
        )
        cmdBtnSizer.Add(
            self.btnCmdClear,
            proportion=1,
            flag=wx.ALIGN_CENTER | wx.RIGHT | wx.BOTTOM,
            border=5,
        )
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
        progressSizer.Add(
            self.btnCmdAbort, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=5
        )
        progressSizer.Add(
            self.progressbar,
            proportion=1,
            flag=wx.ALIGN_CENTER | wx.RIGHT | wx.TOP | wx.BOTTOM,
            border=5,
        )

        self.panelProgress.SetSizer(progressSizer)
        progressSizer.Fit(self.panelProgress)
        self.outputSizer.Add(self.panelProgress, proportion=0, flag=wx.EXPAND)

        self.outputSizer.Fit(self)
        self.outputSizer.SetSizeHints(self)
        self.panelOutput.SetSizer(self.outputSizer)
        self.outputSizer.FitInside(self.panelOutput)
        if self._gcstyle & GC_PROMPT:
            promptSizer.Fit(self)
            promptSizer.SetSizeHints(self)
            self.panelPrompt.SetSizer(promptSizer)

        # split window
        self.SplitHorizontally(self.panelOutput, self.panelPrompt, 0)
        if not (self._gcstyle & GC_PROMPT):
            self.Unsplit()
        self.SetMinimumPaneSize(self.btnClear.GetSize()[1] + 100)

        self.SetSashGravity(1.0)

        self.outputSizer.Hide(self.panelProgress)
        # layout
        self.SetAutoLayout(True)
        self.Layout()

    def GetPanel(self, prompt=True):
        """Get panel

        :param prompt: get prompt / output panel

        :return: wx.Panel reference
        """
        if prompt:
            return self.panelPrompt

        return self.panelOutput

    def WriteLog(
        self, text, style=None, wrap=None, notification=Notification.HIGHLIGHT
    ):
        """Generic method for writing log message in
        given style.

        Emits contentChanged signal.

        :param line: text line
        :param style: text style (see GStc)
        :param stdout: write to stdout or stderr
        :param notification: form of notification
        """

        self.cmdOutput.SetStyle()

        # documenting old behavior/implementation:
        # switch notebook if required
        # now, let user to bind to the old event

        if not style:
            style = self.cmdOutput.StyleDefault

        # p1 = self.cmdOutput.GetCurrentPos()
        p1 = self.cmdOutput.GetEndStyled()
        # self.cmdOutput.GotoPos(p1)
        self.cmdOutput.DocumentEnd()

        for line in text.splitlines():
            # fill space
            if len(line) < self.lineWidth:
                diff = self.lineWidth - len(line)
                line += diff * " "

            self.cmdOutput.AddTextWrapped(line, wrap=wrap)  # adds '\n'

            p2 = self.cmdOutput.GetCurrentPos()

            # between wxWidgets 3.0 and 3.1 they dropped mask param
            try:
                self.cmdOutput.StartStyling(p1)
            except TypeError:
                self.cmdOutput.StartStyling(p1, 0xFF)
            self.cmdOutput.SetStyling(p2 - p1, style)

        self.cmdOutput.EnsureCaretVisible()

        self.contentChanged.emit(notification=notification)

    def WriteCmdLog(self, text, pid=None, notification=Notification.MAKE_VISIBLE):
        """Write message in selected style

        :param text: message to be printed
        :param pid: process pid or None
        :param switchPage: True to switch page
        """
        if pid:
            text = "(" + str(pid) + ") " + text
        self.WriteLog(
            text, style=self.cmdOutput.StyleCommand, notification=notification
        )

    def WriteWarning(self, text):
        """Write message in warning style"""
        self.WriteLog(
            text,
            style=self.cmdOutput.StyleWarning,
            notification=Notification.MAKE_VISIBLE,
        )

    def WriteError(self, text):
        """Write message in error style"""
        self.WriteLog(
            text,
            style=self.cmdOutput.StyleError,
            notification=Notification.MAKE_VISIBLE,
        )

    def OnClear(self, event):
        """Clear content of output window and command window"""
        self.cmdOutput.SetReadOnly(False)
        self.cmdOutput.ClearAll()
        self.cmdOutput.SetReadOnly(True)
        self.progressbar.SetValue(0)
        self.cmdPrompt.CmdErase()

    def GetProgressBar(self):
        """Return progress bar widget"""
        return self.progressbar

    def OnOutputSave(self, event):
        """Save (selected) text from output window to the file"""
        text = self.cmdOutput.GetSelectedText()
        if not text:
            text = self.cmdOutput.GetText()

        # add newline if needed
        if len(text) > 0 and text[-1] != "\n":
            text += "\n"

        dlg = wx.FileDialog(
            self,
            message=_("Save file as..."),
            defaultFile="grass_cmd_output.txt",
            wildcard=_("%(txt)s (*.txt)|*.txt|%(files)s (*)|*")
            % {"txt": _("Text files"), "files": _("Files")},
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        )

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

            try:
                output = open(path, "w")
                output.write(text)
            except OSError as e:
                GError(
                    _("Unable to write file '%(path)s'.\n\nDetails: %(error)s")
                    % {"path": path, "error": e}
                )
            finally:
                output.close()
            message = _("Command output saved into '%s'") % path
            self.showNotification.emit(message=message)

        dlg.Destroy()

    def SetCopyingOfSelectedText(self, copy):
        """Enable or disable copying of selected text in to clipboard.
        Effects prompt and output.

        :param bool copy: True for enable, False for disable
        """
        if copy:
            self.cmdPrompt.Bind(
                stc.EVT_STC_PAINTED, self.cmdPrompt.OnTextSelectionChanged
            )
            self.cmdOutput.Bind(
                stc.EVT_STC_PAINTED, self.cmdOutput.OnTextSelectionChanged
            )
        else:
            self.cmdPrompt.Unbind(stc.EVT_STC_PAINTED)
            self.cmdOutput.Unbind(stc.EVT_STC_PAINTED)

    def OnCmdOutput(self, event):
        """Prints command output.

        Emits contentChanged signal.
        """
        message = event.text
        type = event.type

        self.cmdOutput.AddStyledMessage(message, type)

        if event.type in {"warning", "error"}:
            self.contentChanged.emit(notification=Notification.MAKE_VISIBLE)
        else:
            self.contentChanged.emit(notification=Notification.HIGHLIGHT)

    def OnCmdProgress(self, event):
        """Update progress message info"""
        self.progressbar.SetValue(event.value)
        event.Skip()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
    def OnCmdExportHistory(self, event):
        """Export the history of executed commands stored
        in a .wxgui_history file to a selected file."""
        dlg = wx.FileDialog(
            self,
            message=_("Save file as..."),
            defaultFile="grass_cmd_log.txt",
            wildcard=_("{txt} (*.txt)|*.txt|{files} (*)|*").format(
                txt=_("Text files"), files=_("Files")
            ),
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        )

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if self.cmdPrompt.CopyHistory(path):
                self.showNotification.emit(
                    message=_("Command history saved to '{}'".format(path))
                )

        dlg.Destroy()
        event.Skip()

>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
    def OnCmdRun(self, event):
        """Run command"""
        self.outputSizer.Show(self.panelProgress)
        self.outputSizer.Layout()
        event.Skip()

    def OnCmdDone(self, event):
        """Command done (or aborted)"""
        self.progressbar.SetValue(0)  # reset progress bar on '0%'
        wx.CallLater(100, self._hideProgress)
        event.Skip()

    def _hideProgress(self):
        self.outputSizer.Hide(self.panelProgress)
        self.outputSizer.Layout()

    def ResetFocus(self):
        """Reset focus"""
        self.cmdPrompt.SetFocus()

    def GetPrompt(self):
        """Get prompt"""
        return self.cmdPrompt


class GStc(stc.StyledTextCtrl):
    """Styled text control for GRASS stdout and stderr.

    Based on FrameOutErr.py

    Name:      FrameOutErr.py
    Purpose:   Redirecting stdout / stderr
    Author:    Jean-Michel Fauth, Switzerland
    Copyright: (c) 2005-2007 Jean-Michel Fauth
    Licence:   GPL
    """

    def __init__(self, parent, id, margin=False, wrap=None):
        stc.StyledTextCtrl.__init__(self, parent, id)
        self.parent = parent
        self.SetUndoCollection(True)
        self.SetReadOnly(True)

        # remember position of line beginning (used for '\r')
        self.linePos = -1

        #
        # styles
        #
        self.SetStyle()

        #
        # line margins
        #
        # TODO print number only from cmdlog
        self.SetMarginWidth(1, 0)
        self.SetMarginWidth(2, 0)
        if margin:
            self.SetMarginType(0, stc.STC_MARGIN_NUMBER)
            self.SetMarginWidth(0, 30)
        else:
            self.SetMarginWidth(0, 0)

        #
        # miscellaneous
        #
        self.SetViewWhiteSpace(False)
        self.SetTabWidth(4)
        self.SetUseTabs(False)
        self.UsePopUp(True)
        self.SetSelBackground(
            True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT)
        )
        self.SetUseHorizontalScrollBar(True)

        #
        # bindings
        #
        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)

    def OnTextSelectionChanged(self, event):
        """Copy selected text to clipboard and skip event.
        The same function is in TextCtrlAutoComplete class (prompt.py).
        """
        wx.CallAfter(self.Copy)
        event.Skip()

    def SetStyle(self):
        """Set styles for styled text output windows with type face
        and point size selected by user (Courier New 10 is default)"""

        typeface = UserSettings.Get(group="appearance", key="outputfont", subkey="type")
        if typeface == "":
            typeface = "Courier New"

        typesize = UserSettings.Get(group="appearance", key="outputfont", subkey="size")
        if typesize is None or int(typesize) <= 0:
            typesize = 10
        typesize = int(float(typesize))

        fontInfo = wx.FontInfo(typesize)
        fontInfo.FaceName(typeface)
        fontInfo.Family(wx.FONTFAMILY_TELETYPE)
        defaultFont = wx.Font(fontInfo)

        self.StyleClearAll()

        isDarkMode = False
        if wxPythonPhoenix and CheckWxVersion([4, 1, 0]):
            isDarkMode = wx.SystemSettings.GetAppearance().IsDark()

        defaultBackgroundColour = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW)
        defaultTextColour = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)

        self.StyleDefault = 0
        self.StyleSetFont(stc.STC_STYLE_DEFAULT, defaultFont)
        self.StyleSetBackground(stc.STC_STYLE_DEFAULT, defaultBackgroundColour)
        self.StyleSetForeground(stc.STC_STYLE_DEFAULT, defaultTextColour)

        self.StyleCommand = 1
        self.StyleSetBackground(self.StyleCommand, wx.Colour(154, 154, 154, 255))
        self.StyleSetForeground(self.StyleCommand, defaultTextColour)

        self.StyleOutput = 2
        self.StyleSetBackground(self.StyleOutput, defaultBackgroundColour)
        self.StyleSetForeground(self.StyleOutput, defaultTextColour)

        # fatal error
        self.StyleError = 3
        errorColour = wx.Colour(127, 0, 0)
        if isDarkMode:
            errorColour = wx.Colour(230, 0, 0)
        self.StyleSetBackground(self.StyleError, defaultBackgroundColour)
        self.StyleSetForeground(self.StyleError, errorColour)

        # warning
        self.StyleWarning = 4
        warningColour = wx.Colour(0, 0, 255)
        if isDarkMode:
            warningColour = wx.Colour(0, 102, 255)
        self.StyleSetBackground(self.StyleWarning, defaultBackgroundColour)
        self.StyleSetForeground(self.StyleWarning, warningColour)

        # message
        self.StyleMessage = 5
        self.StyleSetBackground(self.StyleMessage, defaultBackgroundColour)
        self.StyleSetForeground(self.StyleMessage, defaultTextColour)

        # unknown
        self.StyleUnknown = 6
        self.StyleSetBackground(self.StyleUnknown, defaultBackgroundColour)
        self.StyleSetForeground(self.StyleUnknown, defaultTextColour)

    def OnDestroy(self, evt):
        """The clipboard contents can be preserved after
        the app has exited"""

        if wx.TheClipboard.IsOpened():
            wx.TheClipboard.Flush()
        evt.Skip()

    def AddTextWrapped(self, txt, wrap=None):
        """Add string to text area.

        String is wrapped and linesep is also added to the end
        of the string"""
        # allow writing to output window
        self.SetReadOnly(False)

        if wrap:
            txt = textwrap.fill(txt, wrap) + "\n"
        elif txt[-1] != "\n":
            txt += "\n"

        if "\r" in txt:
            self.linePos = -1
            for seg in txt.split("\r"):
                if self.linePos > -1:
                    self.SetCurrentPos(self.linePos)
                    self.ReplaceSelection(seg)
                else:
                    self.linePos = self.GetCurrentPos()
                    self.AddText(seg)
        else:
            self.linePos = self.GetCurrentPos()
            self.AddText(txt)

        # reset output window to read only
        self.SetReadOnly(True)

    def AddStyledMessage(self, message, style=None):
        """Add message to text area.

        Handles messages with progress percentages.

        :param message: message to be added
        :param style: style of message, allowed values: 'message',
                      'warning', 'error' or None
        """
        # message prefix
        if style == "warning":
            message = "WARNING: " + message
        elif style == "error":
            message = "ERROR: " + message

        p1 = self.GetEndStyled()
        self.GotoPos(p1)

        # is this still needed?
        if "\b" in message:
            if self.linePos < 0:
                self.linePos = p1
            last_c = ""
            for c in message:
                if c == "\b":
                    self.linePos -= 1
                else:
                    self.SetCurrentPos(self.linePos)
                    self.ReplaceSelection(c)
                    self.linePos = self.GetCurrentPos()
                    if c != " ":
                        last_c = c
            if last_c not in (digits):
                self.AddTextWrapped("\n", wrap=None)
                self.linePos = -1
        else:
            self.linePos = -1  # don't force position
            if "\n" not in message:
                self.AddTextWrapped(message, wrap=60)
            else:
                self.AddTextWrapped(message, wrap=None)
        p2 = self.GetCurrentPos()

        if p2 >= p1:
            try:
                self.StartStyling(p1)
            except TypeError:
                self.StartStyling(p1, 0xFF)

            if style == "error":
                self.SetStyling(p2 - p1, self.StyleError)
            elif style == "warning":
                self.SetStyling(p2 - p1, self.StyleWarning)
            elif style == "message":
                self.SetStyling(p2 - p1, self.StyleMessage)
            else:  # unknown
                self.SetStyling(p2 - p1, self.StyleUnknown)

        self.EnsureCaretVisible()


class GConsoleFrame(wx.Frame):
    """Standalone GConsole for testing only"""

    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        title="GConsole Test Frame",
        style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        **kwargs,
    ):
        wx.Frame.__init__(self, parent=parent, id=id, title=title, style=style)

        panel = wx.Panel(self, id=wx.ID_ANY)

        from lmgr.menudata import LayerManagerMenuData

        menuTreeBuilder = LayerManagerMenuData()
        self.gconsole = GConsole(guiparent=self)
        self.goutput = GConsoleWindow(
            parent=panel,
            gconsole=self.gconsole,
            menuModel=menuTreeBuilder.GetModel(),
            gcstyle=GC_PROMPT,
        )

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.goutput, proportion=1, flag=wx.EXPAND, border=0)

        panel.SetSizer(mainSizer)
        mainSizer.Fit(panel)
        self.SetMinSize((550, 500))


def testGConsole():
    app = wx.App()
    frame = GConsoleFrame(parent=None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    testGConsole()
