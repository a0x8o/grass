"""
@package vdigit.mapwindow

@brief Map display canvas for wxGUI vector digitizer

Classes:
 - mapwindow::VDigitWindow

(C) 2011-2013 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Martin Landa <landa.martin gmail.com>
"""

import wx
import tempfile

from grass.pydispatch.signal import Signal

from dbmgr.dialogs import DisplayAttributesDialog
from core.gcmd import RunCommand, GMessage, GError
from core.debug import Debug
from mapwin.buffered import BufferedMapWindow
from core.settings import UserSettings
from core.utils import ListOfCatsToRange
from core.units import ConvertValue as UnitsConvertValue
from core.globalvar import QUERYLAYER
from vdigit.dialogs import (
    VDigitCategoryDialog,
    VDigitZBulkDialog,
    VDigitDuplicatesDialog,
)
from gui_core import gselect
from gui_core.wrap import PseudoDC, NewId


class VDigitWindow(BufferedMapWindow):
    """A Buffered window extended for vector digitizer."""

    def __init__(
        self,
        parent,
        giface,
        Map,
        properties,
        tree=None,
        id=wx.ID_ANY,
        lmgr=None,
        style=wx.NO_FULL_REPAINT_ON_RESIZE,
        **kwargs,
    ):
        BufferedMapWindow.__init__(
            self,
            parent=parent,
            giface=giface,
            Map=Map,
            properties=properties,
            style=style,
            **kwargs,
        )
        self.lmgr = lmgr
        self.tree = tree
        self.pdcVector = PseudoDC()
        self.toolbar = self.parent.GetToolbar("vdigit")
        self.digit = None  # wxvdigit.IVDigit
        self._digitizingInfo = False  # digitizing with info

        # Emitted when info about digitizing updated
        # Parameter text is a string with information
        # currently used only for coordinates of mouse cursor + segmnt and
        # total feature length
        self.digitizingInfo = Signal("VDigitWindow.digitizingInfo")
        # Emitted when some info about digitizing is or will be available
        self.digitizingInfoAvailable = Signal("VDigitWindow.digitizingInfo")
        # Emitted when some info about digitizing is or will be available
        # digitizingInfo signal is emitted only between digitizingInfoAvailable
        # and digitizingInfoUnavailable signals
        self.digitizingInfoUnavailable = Signal("VDigitWindow.digitizingInfo")

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.mouseMoving.connect(self._mouseMovingToDigitizingInfo)

    def GetDisplay(self):
        if self.digit:
            return self.digit.GetDisplay()
        return None

    def GetDigit(self):
        """Get digit class"""
        return self.digit

    def SetToolbar(self, toolbar):
        """Set up related toolbar"""
        self.toolbar = toolbar

    def _mouseMovingToDigitizingInfo(self, x, y):
        e, n = x, y
        precision = int(
            UserSettings.Get(group="projection", key="format", subkey="precision")
        )
        if (
            self.toolbar.GetAction() != "addLine"
            or self.toolbar.GetAction("type") not in {"line", "boundary"}
            or len(self.polycoords) == 0
        ):
            # we cannot provide info, so find out if it is something new
            if self._digitizingInfo:
                self._digitizingInfo = False
                self.digitizingInfoUnavailable.emit()
            return
        # else, we can provide info, so find out if it is first time
        if not self._digitizingInfo:
            self._digitizingInfo = True
            self.digitizingInfoAvailable.emit()

        # for linear feature show segment and total length
        distance_seg = self.Distance(self.polycoords[-1], (e, n), screen=False)[0]
        distance_tot = distance_seg
        for idx in range(1, len(self.polycoords)):
            distance_tot += self.Distance(
                self.polycoords[idx - 1], self.polycoords[idx], screen=False
            )[0]
        text = "seg: %.*f; tot: %.*f" % (
            precision,
            distance_seg,
            precision,
            distance_tot,
        )
        self.digitizingInfo.emit(text=text)

    def OnKeyDown(self, event):
        """Key pressed"""
        shift = event.ShiftDown()
        kc = event.GetKeyCode()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
        default_tools = {
            "addPoint": {
                "evt": True,
                "ord": ord("P"),
                "tool": self.toolbar.OnAddPoint,
            },
            "addLine": {
                "evt": True,
                "ord": ord("L"),
                "tool": self.toolbar.OnAddLine,
            },
            "addArea": {
                "evt": True,
                "ord": ord("A"),
                "tool": self.toolbar.OnAddArea,
            },
            "addBoundary": {
                "evt": False,
                "ord": ord("B"),
                "tool": self.toolbar.OnAddBoundary,
            },
            "addCentroid": {
                "evt": False,
                "ord": ord("C"),
                "tool": self.toolbar.OnAddCentroid,
            },
            "addVertex": {
                "evt": True,
                "ord": ord("V"),
                "tool": self.toolbar.OnAddVertex,
            },
            "removeVertex": {
                "evt": True,
                "ord": ord("X"),
                "tool": self.toolbar.OnRemoveVertex,
            },
            "moveVertex": {
                "evt": True,
                "ord": ord("G"),
                "tool": self.toolbar.OnMoveVertex,
            },
            "deleteLine": {
                "evt": True,
                "ord": ord("D"),
                "tool": self.toolbar.OnDeleteLine,
            },
            "deleteArea": {
                "evt": True,
                "ord": ord("F"),
                "tool": self.toolbar.OnDeleteArea,
            },
            "editLine": {
                "evt": True,
                "ord": ord("E"),
                "tool": self.toolbar.OnEditLine,
            },
            "moveLine": {
                "evt": True,
                "ord": ord("M"),
                "tool": self.toolbar.OnMoveLine,
            },
            "displayCats": {
                "evt": True,
                "ord": ord("J"),
                "tool": self.toolbar.OnDisplayCats,
            },
            "displayAttr": {
                "evt": True,
                "ord": ord("K"),
                "tool": self.toolbar.OnDisplayAttr,
            },
            "undo": {
                "evt": True,
                "ord": ord("Z"),
                "tool": self.toolbar.OnUndo,
            },
            "redo": {
                "evt": True,
                "ord": ord("Y"),
                "tool": self.toolbar.OnRedo,
            },
            "settings": {
                "evt": True,
                "ord": ord("T"),
                "tool": self.toolbar.OnSettings,
            },
            "help": {
                "evt": True,
                "ord": ord("H"),
                "tool": self.toolbar.OnHelp,
            },
            "quit": {
                "evt": True,
                "ord": ord("Q"),
                "tool": self.toolbar.OnExit,
            },
        }

        # Custom vdigit tools if VDigitToolbar class tool param arg was defined
        actual_tools = {}
        for tool in default_tools:
            # custom tools, e.g. in g.gui.iclass
            if self.toolbar.tools and tool not in self.toolbar.tools:
                continue
            event = None
            if default_tools[tool]["evt"] and hasattr(self.toolbar, tool):
                event = wx.CommandEvent(id=getattr(self.toolbar, tool))
            actual_tools[default_tools[tool]["ord"]] = {
                "event": event,
                "tool": default_tools[tool]["tool"],
            }

        if not shift:
            tool = actual_tools.get(kc)
=======
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
        tools = {
            ord("P"): {
                "event": wx.CommandEvent(id=self.toolbar.addPoint),
                "tool": self.toolbar.OnAddPoint,
            },
            ord("L"): {
                "event": wx.CommandEvent(id=self.toolbar.addLine),
                "tool": self.toolbar.OnAddLine,
            },
            ord("A"): {
                "event": wx.CommandEvent(id=self.toolbar.addArea),
                "tool": self.toolbar.OnAddArea,
            },
            ord("B"): {
                "event": None,
                "tool": self.toolbar.OnAddBoundary,
            },
            ord("C"): {
                "event": None,
                "tool": self.toolbar.OnAddCentroid,
            },
            ord("V"): {
                "event": wx.CommandEvent(id=self.toolbar.addVertex),
                "tool": self.toolbar.OnAddVertex,
            },
            ord("X"): {
                "event": wx.CommandEvent(id=self.toolbar.removeVertex),
                "tool": self.toolbar.OnRemoveVertex,
            },
            ord("G"): {
                "event": wx.CommandEvent(id=self.toolbar.moveVertex),
                "tool": self.toolbar.OnMoveVertex,
            },
            ord("D"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteLine),
                "tool": self.toolbar.OnDeleteLine,
            },
            ord("F"): {
                "event": wx.CommandEvent(id=self.toolbar.deleteArea),
                "tool": self.toolbar.OnDeleteArea,
            },
            ord("E"): {
                "event": wx.CommandEvent(id=self.toolbar.editLine),
                "tool": self.toolbar.OnEditLine,
            },
            ord("M"): {
                "event": wx.CommandEvent(id=self.toolbar.moveLine),
                "tool": self.toolbar.OnMoveLine,
            },
            ord("J"): {
                "event": wx.CommandEvent(id=self.toolbar.displayCats),
                "tool": self.toolbar.OnDisplayCats,
            },
            ord("K"): {
                "event": wx.CommandEvent(id=self.toolbar.displayAttr),
                "tool": self.toolbar.OnDisplayAttr,
            },
            ord("Z"): {
                "event": wx.CommandEvent(id=self.toolbar.undo),
                "tool": self.toolbar.OnUndo,
            },
            ord("Y"): {
                "event": wx.CommandEvent(id=self.toolbar.redo),
                "tool": self.toolbar.OnRedo,
            },
            ord("T"): {
                "event": wx.CommandEvent(id=self.toolbar.settings),
                "tool": self.toolbar.OnSettings,
            },
            ord("H"): {
                "event": wx.CommandEvent(id=self.toolbar.help),
                "tool": self.toolbar.OnHelp,
            },
            ord("Q"): {
                "event": wx.CommandEvent(id=self.toolbar.quit),
                "tool": self.toolbar.OnExit,
            },
        }
        if not shift:
            tool = tools.get(kc)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
            if tool:
                event = self.toolbar.OnTool(tool["event"])
                tool["tool"](event)

    def _updateMap(self):
        if not self.toolbar or not self.toolbar.GetLayer():
            return

        # set region
        self.digit.GetDisplay().UpdateRegion()
        # re-calculate threshold for digitization tool
        # self.parent.digit.GetDisplay().GetThreshold()
        # draw map
        # self.pdcVector.Clear()
        self.pdcVector.RemoveAll()

        item = None
        if self.tree:
            try:
                item = self.tree.FindItemByData("maplayer", self.toolbar.GetLayer())
            except TypeError:
                pass

        if not self.tree or (self.tree and item and self.tree.IsItemChecked(item)):
            self.redrawAll = True
            self.digit.GetDisplay().DrawMap()

        # translate tmp objects (pointer position)
        if self.toolbar.GetAction() == "moveLine" and hasattr(self, "moveInfo"):
            if "beginDiff" in self.moveInfo:
                # move line
                for id in self.moveInfo["id"]:
                    self.pdcTmp.TranslateId(
                        id, self.moveInfo["beginDiff"][0], self.moveInfo["beginDiff"][1]
                    )
                del self.moveInfo["beginDiff"]

    def OnLeftDownAddLine(self, event):
        """Left mouse button pressed - add new feature"""
        try:
            mapLayer = self.toolbar.GetLayer().GetName()
        except:
            return

        if self.toolbar.GetAction("type") in {"point", "centroid"}:
            # add new point / centroid
            east, north = self.Pixel2Cell(self.mouse["begin"])
            nfeat, fids = self.digit.AddFeature(
                self.toolbar.GetAction("type"), [(east, north)]
            )
            if nfeat < 1:
                return

            self.UpdateMap(render=False)  # redraw map

            # add new record into attribute table
            if UserSettings.Get(group="vdigit", key="addRecord", subkey="enabled"):
                # select attributes based on layer and category
                cats = {
                    fids[0]: {
                        UserSettings.Get(group="vdigit", key="layer", subkey="value"): (
                            UserSettings.Get(
                                group="vdigit", key="category", subkey="value"
                            ),
                        )
                    }
                }

                posWindow = self.ClientToScreen(
                    (
                        self.mouse["end"][0] + self.dialogOffset,
                        self.mouse["end"][1] + self.dialogOffset,
                    )
                )

                addRecordDlg = DisplayAttributesDialog(
                    parent=self,
                    map=mapLayer,
                    cats=cats,
                    pos=posWindow,
                    action="add",
                    ignoreError=True,
                )

                if self.toolbar.GetAction("type") == "centroid":
                    for fid in fids:
                        self._geomAttrb(fid, addRecordDlg, "area")
                        self._geomAttrb(fid, addRecordDlg, "perimeter")

                if addRecordDlg.IsFound():
                    addRecordDlg.ShowModal()
                addRecordDlg.Destroy()

        elif self.toolbar.GetAction("type") in {"line", "boundary", "area"}:
            # add new point to the line
            self.polycoords.append(self.Pixel2Cell(event.GetPosition()))
            self.DrawLines(pdc=self.pdcTmp)

    def _geomAttrb(self, fid, dialog, attrb):
        """Define geometry attributes"""
        mapLayer = self.toolbar.GetLayer()
        if self.tree:
            item = self.tree.FindItemByData("maplayer", mapLayer)
            vdigit = self.tree.GetLayerInfo(item, key="vdigit")
        else:
            item = vdigit = None

        if not vdigit or "geomAttr" not in vdigit or attrb not in vdigit["geomAttr"]:
            return

        val = -1
        if attrb == "length":
            val = self.digit.GetLineLength(fid)
            type = attrb
        elif attrb == "area":
            val = self.digit.GetAreaSize(fid)
            type = attrb
        elif attrb == "perimeter":
            val = self.digit.GetAreaPerimeter(fid)
            type = "length"

        if val > 0:
            layer = int(UserSettings.Get(group="vdigit", key="layer", subkey="value"))
            column = vdigit["geomAttr"][attrb]["column"]
            val = UnitsConvertValue(val, type, vdigit["geomAttr"][attrb]["units"])
            dialog.SetColumnValue(layer, column, val)
            dialog.OnReset()

    def _geomAttrbUpdate(self, fids):
        """Update geometry attributes of currently selected features

        :param fid: list feature id
        """
        mapLayer = self.parent.toolbars["vdigit"].GetLayer()
        vectorName = mapLayer.GetName()
        if self.tree:
            item = self.tree.FindItemByData("maplayer", mapLayer)
            vdigit = self.tree.GetLayerInfo(item, key="vdigit")
        else:
            item = vdigit = None

        if not vdigit or "geomAttr" not in vdigit:
            return

        dbInfo = gselect.VectorDBInfo(vectorName)
        sqlfile = tempfile.NamedTemporaryFile(mode="w")
        for fid in fids:
            for layer, cats in self.digit.GetLineCats(fid).items():
                table = dbInfo.GetTable(layer)
                for attrb, item in vdigit["geomAttr"].items():
                    val = -1
                    if attrb == "length":
                        val = self.digit.GetLineLength(fid)
                        type = attrb
                    elif attrb == "area":
                        val = self.digit.GetAreaSize(fid)
                        type = attrb
                    elif attrb == "perimeter":
                        val = self.digit.GetAreaPerimeter(fid)
                        type = "length"

                    if val < 0:
                        continue
                    val = UnitsConvertValue(val, type, item["units"])

                    for cat in cats:
                        sqlfile.write(
                            "UPDATE %s SET %s = %f WHERE %s = %d;\n"
                            % (
                                table,
                                item["column"],
                                val,
                                dbInfo.GetKeyColumn(layer),
                                cat,
                            )
                        )

            sqlfile.file.flush()
            RunCommand("db.execute", parent=True, quiet=True, input=sqlfile.name)

    def _updateATM(self):
        """Update open Attribute Table Manager

        .. todo::
            use AddDataRow() instead
        """
        if not self.lmgr:
            return

        # update ATM
        digitVector = self.toolbar.GetLayer().GetName()

        for atm in self.lmgr.dialogs["atm"]:
            atmVector = atm.GetVectorName()
            if atmVector == digitVector:
                layer = UserSettings.Get(group="vdigit", key="layer", subkey="value")
                # TODO: use AddDataRow instead
                atm.LoadData(layer)

    def OnLeftDownEditLine(self, event):
        """Left mouse button pressed - edit linear feature - add new
        vertex.
        """
        self.polycoords.append(self.Pixel2Cell(self.mouse["begin"]))
        self.moveInfo["id"].append(NewId())
        self.DrawLines(pdc=self.pdcTmp)

    def OnLeftDownMoveLine(self, event):
        """Left mouse button pressed - vector digitizer move
        feature/vertex, edit linear feature
        """
        self.moveInfo = {}
        # geographic coordinates of initial position (left-down)
        self.moveInfo["begin"] = None
        # list of ids to modify
        self.moveInfo["id"] = []

        # set pen
        if self.toolbar.GetAction() in {"moveVertex", "editLine"}:
            pcolor = UserSettings.Get(
                group="vdigit", key="symbol", subkey=["highlight", "color"]
            )
            self.pen = self.polypen = wx.Pen(
                colour=pcolor, width=2, style=wx.SHORT_DASH
            )
            self.pdcTmp.SetPen(self.polypen)

    def OnLeftDownDisplayCA(self, event):
        """Left mouse button pressed - vector digitizer display categories
        or attributes action
        """
        try:
            mapLayer = self.toolbar.GetLayer().GetName()
        except:
            return

        coords = self.Pixel2Cell(self.mouse["begin"])

        # unselect
        self.digit.GetDisplay().SetSelected([])

        # select feature by point
        cats = {}
        self.digit.GetDisplay().SelectLineByPoint(coords)

        if not self.digit.GetDisplay().GetSelected():
            for key in ("attributes", "category"):
                if self.parent.dialogs[key] and self.parent.dialogs[key].IsShown():
                    self.parent.dialogs[key].Hide()
            self.UpdateMap(render=False, renderVector=True)
            return

        if UserSettings.Get(group="vdigit", key="checkForDupl", subkey="enabled"):
            lines = self.digit.GetDisplay().GetSelected()
        else:
            lines = (self.digit.GetDisplay().GetSelected()[0],)  # only first found

        for line in lines:
            cats[line] = self.digit.GetLineCats(line)

        posWindow = self.ClientToScreen(
            (
                self.mouse["end"][0] + self.dialogOffset,
                self.mouse["end"][1] + self.dialogOffset,
            )
        )

        if self.toolbar.GetAction() == "displayAttrs":
            # select attributes based on coordinates (all layers)
            if self.parent.dialogs["attributes"] is None:
                self.parent.dialogs["attributes"] = DisplayAttributesDialog(
                    parent=self, map=mapLayer, cats=cats, action="update"
                )
            else:
                # upgrade dialog
                self.parent.dialogs["attributes"].UpdateDialog(cats=cats)

            if (
                self.parent.dialogs["attributes"]
                and self.parent.dialogs["attributes"].mapDBInfo
            ):
                if len(cats.keys()) > 0:
                    # highlight feature & re-draw map
                    if not self.parent.dialogs["attributes"].IsShown():
                        self.parent.dialogs["attributes"].Show()
                else:  # noqa: PLR5501
                    if (
                        self.parent.dialogs["attributes"]
                        and self.parent.dialogs["attributes"].IsShown()
                    ):
                        self.parent.dialogs["attributes"].Hide()

        else:  # displayCats
            if self.parent.dialogs["category"] is None:
                # open new dialog
                dlg = VDigitCategoryDialog(
                    parent=self,
                    vectorName=mapLayer,
                    cats=cats,
                    pos=posWindow,
                    title=_("Update categories"),
                )
                self.parent.dialogs["category"] = dlg
            else:
                # update currently open dialog
                self.parent.dialogs["category"].UpdateDialog(cats=cats)

            if self.parent.dialogs["category"]:
                if len(cats.keys()) > 0:
                    # highlight feature & re-draw map
                    if not self.parent.dialogs["category"].IsShown():
                        self.parent.dialogs["category"].Show()
                else:  # noqa: PLR5501
                    if self.parent.dialogs["category"].IsShown():
                        self.parent.dialogs["category"].Hide()

        self.UpdateMap(render=False, renderVector=True)

    def OnLeftDownCopyCA(self, event):
        """Left mouse button pressed - vector digitizer copy
        categories or attributes action
        """
        if not hasattr(self, "copyCatsList"):
            self.copyCatsList = []
        else:
            self.copyCatsIds = []
            self.mouse["box"] = "box"

    def OnLeftDownCopyLine(self, event):
        """Left mouse button pressed - vector digitizer copy lines
        action
        """
        if not hasattr(self, "copyIds"):
            self.copyIds = []
            self.layerTmp = None

    def OnLeftDownBulkLine(self, event):
        """Left mouse button pressed - vector digitizer label 3D
        vector lines
        """
        if len(self.polycoords) > 1:  # start new line
            self.polycoords = []
            self.ClearLines(pdc=self.pdcTmp)
        self.polycoords.append(self.Pixel2Cell(event.GetPosition()))
        if len(self.polycoords) == 1:
            begin = self.Pixel2Cell(self.polycoords[-1])
            end = self.Pixel2Cell(self.mouse["end"])
        else:
            end = self.Pixel2Cell(self.polycoords[-1])
            begin = self.Pixel2Cell(self.mouse["begin"])

            self.DrawLines(self.pdcTmp, polycoords=(begin, end))

    def OnLeftDownUndo(self, event):
        """Left mouse button pressed with control key - vector
        digitizer undo functionality
        """
        if self.mouse["use"] != "pointer" or not self.toolbar:
            return

        action = self.toolbar.GetAction()
        if (
            action == "addLine"
            and self.toolbar.GetAction("type") in {"line", "boundary", "area"}
        ) or action == "editLine":
            # add line or boundary -> remove last point from the line
            try:
                removed = self.polycoords.pop()
                Debug.msg(
                    4,
                    "VDigitWindow.OnMiddleDown(): polycoords_poped=%s"
                    % [
                        removed,
                    ],
                )
                # self.mouse['begin'] = self.Cell2Pixel(self.polycoords[-1])
            except:
                pass

        if action == "editLine":
            # remove last vertex & line
            if len(self.moveInfo["id"]) > 1:
                self.moveInfo["id"].pop()

            self.UpdateMap(render=False, renderVector=False)

        elif action in {
            "deleteLine",
            "deleteArea",
            "moveLine",
            "splitLine",
            "addVertex",
            "removeVertex",
            "moveVertex",
            "copyCats",
            "flipLine",
            "mergeLine",
            "snapLine",
            "connectLine",
            "copyLine",
            "queryLine",
            "breakLine",
            "typeConv",
        }:
            # various tools -> unselected selected features
            self.digit.GetDisplay().SetSelected([])

            if action in {"moveLine", "moveVertex", "editLine"} and hasattr(
                self, "moveInfo"
            ):
                del self.moveInfo

            elif action == "copyCats":
                try:
                    del self.copyCatsList
                    del self.copyCatsIds
                except AttributeError:
                    pass

            elif action == "copyLine":
                del self.copyIds
                if self.layerTmp:
                    self.Map.DeleteLayer(self.layerTmp)
                    self.UpdateMap(render=True, renderVector=False)
                del self.layerTmp

            self.polycoords = []
            self.UpdateMap(render=False)  # render vector

        elif action == "zbulkLine":
            # reset polyline
            self.polycoords = []
            self.digit.GetDisplay().SetSelected([])
            self.UpdateMap(render=False)

        self.redrawAll = True
        self.UpdateMap(render=False, renderVector=False)

    def _onLeftDown(self, event):
        """Left mouse button donw - vector digitizer various actions"""
        try:
            mapLayer = self.toolbar.GetLayer().GetName()
        except:
            GMessage(parent=self, message=_("No vector map selected for editing."))
            event.Skip()
            return

        action = self.toolbar.GetAction()

        if not action:
            GMessage(
                parent=self,
                message=_(
                    "Nothing to do. Choose appropriate tool from digitizer toolbar."
                ),
            )
            event.Skip()
            return

        if action not in {"moveVertex", "addVertex", "removeVertex", "editLine"}:
            # set pen
            self.pen = wx.Pen(
                colour=UserSettings.Get(
                    group="vdigit", key="symbol", subkey=["newSegment", "color"]
                ),
                width=2,
                style=wx.SHORT_DASH,
            )
            self.polypen = wx.Pen(
                colour=UserSettings.Get(
                    group="vdigit", key="symbol", subkey=["newLine", "color"]
                ),
                width=2,
                style=wx.SOLID,
            )

        if action in {"addVertex", "removeVertex", "splitLines"}:
            # unselect
            self.digit.GetDisplay().SetSelected([])

        if action == "addLine":
            self.OnLeftDownAddLine(event)

        elif action == "editLine" and hasattr(self, "moveInfo"):
            self.OnLeftDownEditLine(event)

        elif action in {"moveLine", "moveVertex", "editLine"} and not hasattr(
            self, "moveInfo"
        ):
            self.OnLeftDownMoveLine(event)

        elif action in ("displayAttrsdisplayCats"):
            self.OnLeftDownDisplayCA(event)

        elif action in {"copyCats", "copyAttrs"}:
            self.OnLeftDownCopyCA(event)

        elif action == "copyLine":
            self.OnLeftDownCopyLine(event)

        elif action == "zbulkLine":
            self.OnLeftDownBulkLine(event)

    def OnLeftUpVarious(self, event):
        """Left mouse button released - vector digitizer various
        actions
        """
        pos1 = self.Pixel2Cell(self.mouse["begin"])
        pos2 = self.Pixel2Cell(self.mouse["end"])

        nselected = 0
        action = self.toolbar.GetAction()
        # -> delete line || move line || move vertex
        if action in {"moveVertex", "editLine"}:
            if len(self.digit.GetDisplay().GetSelected()) == 0:
                nselected = int(
                    self.digit.GetDisplay().SelectLineByPoint(pos1)["line"] != -1
                )

                if action == "editLine":
                    try:
                        selVertex = self.digit.GetDisplay().GetSelectedVertex(pos1)[0]
                    except IndexError:
                        selVertex = None

                    if selVertex:
                        # self.UpdateMap(render=False)
                        ids = self.digit.GetDisplay().GetSelected(grassId=False)
                        # move this line to tmp layer
                        self.polycoords = []
                        for id in ids:
                            if id % 2:  # register only vertices
                                e, n = self.Pixel2Cell(
                                    self.pdcVector.GetIdBounds(id)[0:2]
                                )
                                self.polycoords.append((e, n))
                        self.digit.GetDisplay().DrawSelected(False)

                        if selVertex < ids[-1] / 2:
                            # choose first or last node of line
                            self.moveInfo["id"].reverse()
                            self.polycoords.reverse()
                    else:
                        # unselect
                        self.digit.GetDisplay().SetSelected([])
                        if hasattr(self, "moveInfo"):
                            del self.moveInfo

                    self.UpdateMap(render=False)

        elif action in {"copyCats", "copyAttrs"}:
            if not hasattr(self, "copyCatsIds"):
                # 'from' -> select by point
                nselected = int(
                    self.digit.GetDisplay().SelectLineByPoint(pos1)["line"] != -1
                )
                if nselected:
                    self.copyCatsList = self.digit.GetDisplay().GetSelected()
            else:
                # -> 'to' -> select by bbox
                self.digit.GetDisplay().SetSelected([])
                # return number of selected features (by box/point)
                nselected = self.digit.GetDisplay().SelectLinesByBox((pos1, pos2))
                if nselected == 0:
                    nselected = int(
                        self.digit.GetDisplay().SelectLineByPoint(pos1)["line"] != -1
                    )

                if nselected > 0:
                    self.copyCatsIds = self.digit.GetDisplay().GetSelected()

        elif action == "queryLine":
            selected = self.digit.SelectLinesByQuery(bbox=(pos1, pos2))
            nselected = len(selected)
            if nselected > 0:
                self.digit.GetDisplay().SetSelected(selected)

        # -> moveLine || deleteLine, etc. (select by point/box)
        elif action == "moveLine" and len(self.digit.GetDisplay().GetSelected()) > 0:
            nselected = 0
        elif action == "deleteArea":
            nselected = int(
                self.digit.GetDisplay().SelectAreaByPoint(pos1)["area"] != -1
            )
        else:
            drawSeg = action == "moveLine"

            nselected = self.digit.GetDisplay().SelectLinesByBox(
                bbox=(pos1, pos2), drawSeg=drawSeg
            )
            if nselected == 0:
                nselected = int(
                    self.digit.GetDisplay().SelectLineByPoint(pos1)["line"] != -1
                )

        if nselected > 0:
            if action in {"moveLine", "moveVertex"} and hasattr(self, "moveInfo"):
                # get pseudoDC id of objects which should be redrawn
                if action == "moveLine":
                    # -> move line
                    self.moveInfo["id"] = self.digit.GetDisplay().GetSelected(
                        grassId=False
                    )
                else:  # moveVertex
                    self.moveInfo["id"] = self.digit.GetDisplay().GetSelectedVertex(
                        pos1
                    )
                    if len(self.moveInfo["id"]) == 0:  # no vertex found
                        self.digit.GetDisplay().SetSelected([])

            #
            # check for duplicates
            #
            if UserSettings.Get(group="vdigit", key="checkForDupl", subkey="enabled"):
                dupl = self.digit.GetDisplay().GetDuplicates()
                self.UpdateMap(render=False)

                if dupl:
                    posWindow = self.ClientToScreen(
                        (
                            self.mouse["end"][0] + self.dialogOffset,
                            self.mouse["end"][1] + self.dialogOffset,
                        )
                    )

                    dlg = VDigitDuplicatesDialog(parent=self, data=dupl, pos=posWindow)

                    if dlg.ShowModal() == wx.ID_OK:
                        self.digit.GetDisplay().UnSelect(dlg.GetUnSelected())
                        # update selected
                        self.UpdateMap(render=False)

            if action != "editLine":
                # -> move line || move vertex
                self.UpdateMap(render=False)

<<<<<<< HEAD
        # no vector object found
        elif not (
            action in {"moveLine", "moveVertex"}
            and hasattr(self, "moveInfo")
            and len(self.moveInfo["id"]) > 0
        ):
            # avoid left-click when features are already selected
            self.UpdateMap(render=False, renderVector=False)
=======
        else:  # no vector object found
            if not (
                action in {"moveLine", "moveVertex"}
                and hasattr(self, "moveInfo")
                and len(self.moveInfo["id"]) > 0
            ):
                # avoid left-click when features are already selected
                self.UpdateMap(render=False, renderVector=False)
>>>>>>> 6bd0f720cb (style(gui): Fixes literal-membership (PLR6201) (#3952))

    def OnLeftUpModifyLine(self, event):
        """Left mouse button released - vector digitizer split line,
        add/remove vertex action
        """
        pos1 = self.Pixel2Cell(self.mouse["begin"])

        pointOnLine = self.digit.GetDisplay().SelectLineByPoint(pos1)["point"]
        if not pointOnLine:
            return

        if self.toolbar.GetAction() in {"splitLine", "addVertex"}:
            self.UpdateMap(render=False)  # highlight object
            self.DrawCross(
                pdc=self.pdcTmp,
                coords=self.Cell2Pixel((pointOnLine[0], pointOnLine[1])),
                size=5,
            )
        else:  # removeVertex
            # get only id of vertex
            try:
                id = self.digit.GetDisplay().GetSelectedVertex(pos1)[0]
            except IndexError:
                id = None

            if id:
                x, y = self.pdcVector.GetIdBounds(id)[0:2]
                self.pdcVector.RemoveId(id)
                self.UpdateMap(render=False)  # highlight object
                self.DrawCross(pdc=self.pdcTmp, coords=(x, y), size=5)
            else:
                # unselect
                self.digit.GetDisplay().SetSelected([])
                self.UpdateMap(render=False)

    def OnLeftUpCopyLine(self, event):
        """Left mouse button released - vector digitizer copy feature
        action
        """
        pos1 = self.Pixel2Cell(self.mouse["begin"])
        pos2 = self.Pixel2Cell(self.mouse["end"])

        if (
            UserSettings.Get(
                group="vdigit", key="bgmap", subkey="value", settings_type="internal"
            )
            == ""
        ):
            # no background map -> copy from current vector map layer
            nselected = self.digit.GetDisplay().SelectLinesByBox((pos1, pos2))

            if nselected > 0:
                # highlight selected features
                self.UpdateMap(render=False)
            else:
                self.UpdateMap(render=False, renderVector=False)
        else:
            # copy features from background map
            self.copyIds = self.digit.SelectLinesFromBackgroundMap(bbox=(pos1, pos2))
            if len(self.copyIds) > 0:
                color = UserSettings.Get(
                    group="vdigit", key="symbol", subkey=["highlight", "color"]
                )
                colorStr = str(color[0]) + ":" + str(color[1]) + ":" + str(color[2])
                dVectTmp = [
                    "d.vect",
                    "map=%s"
                    % UserSettings.Get(
                        group="vdigit",
                        key="bgmap",
                        subkey="value",
                        settings_type="internal",
                    ),
                    "cats=%s" % ListOfCatsToRange(self.copyIds),
                    "-i",
                    "color=%s" % colorStr,
                    "fill_color=%s" % colorStr,
                    "type=point,line,boundary,centroid",
                    "width=2",
                ]

                if not self.layerTmp:
                    self.layerTmp = self.Map.AddLayer(
                        ltype="vector", name=QUERYLAYER, command=dVectTmp
                    )
                else:
                    self.layerTmp.SetCmd(dVectTmp)
            elif self.layerTmp:
                self.Map.DeleteLayer(self.layerTmp)
                self.layerTmp = None

            self.UpdateMap(render=True, renderVector=True)

    def OnLeftUpBulkLine(self, event):
        """Left mouse button released - vector digitizer z-bulk line
        action
        """
        # select lines to be labeled
        pos1 = self.polycoords[0]
        pos2 = self.polycoords[1]
        nselected = self.digit.GetDisplay().SelectLinesByBox((pos1, pos2))

        if nselected > 0:
            # highlight selected features
            self.UpdateMap(render=False)
            self.DrawLines(pdc=self.pdcTmp)  # redraw temp line
        else:
            self.UpdateMap(render=False, renderVector=False)

    def OnLeftUpConnectLine(self, event):
        """Left mouse button released - vector digitizer connect line
        action
        """
        if len(self.digit.GetDisplay().GetSelected()) > 0:
            self.UpdateMap(render=False)

    def _onLeftUp(self, event):
        """Left mouse button released"""
        if event.ControlDown():
            return

        if hasattr(self, "moveInfo"):
            if len(self.digit.GetDisplay().GetSelected()) == 0:
                self.moveInfo["begin"] = self.Pixel2Cell(
                    self.mouse["begin"]
                )  # left down

            # eliminate initial mouse moving effect
            self.mouse["begin"] = self.mouse["end"]

        action = self.toolbar.GetAction()
        if action in {
            "deleteLine",
            "deleteArea",
            "moveLine",
            "moveVertex",
            "copyCats",
            "copyAttrs",
            "editLine",
            "flipLine",
            "mergeLine",
            "snapLine",
            "queryLine",
            "breakLine",
            "typeConv",
            "connectLine",
        }:
            self.OnLeftUpVarious(event)

        elif action in {"splitLine", "addVertex", "removeVertex"}:
            self.OnLeftUpModifyLine(event)

        elif action == "copyLine":
            self.OnLeftUpCopyLine(event)

        elif action == "zbulkLine" and len(self.polycoords) == 2:
            self.OnLeftUpBulkLine(event)

        elif action == "connectLine":
            self.OnLeftUpConnectLine(event)

        if len(self.digit.GetDisplay().GetSelected()) > 0:
            self.redrawAll = None

    def _onRightDown(self, event):
        # digitization tool (confirm action)
        action = self.toolbar.GetAction()
        if action in {"moveLine", "moveVertex"} and hasattr(self, "moveInfo"):
            pFrom = self.moveInfo["begin"]
            pTo = self.Pixel2Cell(event.GetPosition())

            move = (pTo[0] - pFrom[0], pTo[1] - pFrom[1])

            if action == "moveLine":
                # move line
                if self.digit.MoveSelectedLines(move) < 0:
                    return
            elif action == "moveVertex":
                # move vertex
                fid = self.digit.MoveSelectedVertex(pFrom, move)
                if fid < 0:
                    return

                self._geomAttrbUpdate(
                    [
                        fid,
                    ]
                )

            del self.moveInfo

    def _onRightUp(self, event):
        """Right mouse button released (confirm action)"""
        action = self.toolbar.GetAction()
        if action == "addLine" and self.toolbar.GetAction("type") in {
            "line",
            "boundary",
            "area",
        }:
            # -> add new line / boundary
            try:
                mapName = self.toolbar.GetLayer().GetName()
            except:
                mapName = None
                GError(parent=self, message=_("No vector map selected for editing."))

            if mapName:
                line = self.toolbar.GetAction("type") == "line"

                if len(self.polycoords) < 2:  # ignore 'one-point' lines
                    return

                nfeat, fids = self.digit.AddFeature(
                    self.toolbar.GetAction("type"), self.polycoords
                )
                if nfeat < 0:
                    return

                position = self.Cell2Pixel(self.polycoords[-1])
                self.polycoords = []
                self.UpdateMap(render=False)
                self.redrawAll = True
                self.Refresh()

                # add new record into attribute table
                if self._addRecord() and (line is True or (not line and nfeat > 0)):
                    posWindow = self.ClientToScreen(
                        (
                            position[0] + self.dialogOffset,
                            position[1] + self.dialogOffset,
                        )
                    )

                    # select attributes based on layer and category
                    cats = {
                        fids[0]: {
                            UserSettings.Get(
                                group="vdigit", key="layer", subkey="value"
                            ): (
                                UserSettings.Get(
                                    group="vdigit", key="category", subkey="value"
                                ),
                            )
                        }
                    }

                    addRecordDlg = DisplayAttributesDialog(
                        parent=self,
                        map=mapName,
                        cats=cats,
                        pos=posWindow,
                        action="add",
                        ignoreError=True,
                    )

                    for fid in fids:
                        self._geomAttrb(fid, addRecordDlg, "length")
                        # auto-placing centroid
                        self._geomAttrb(fid, addRecordDlg, "area")
                        self._geomAttrb(fid, addRecordDlg, "perimeter")

                    if addRecordDlg.IsFound():
                        addRecordDlg.ShowModal()
                    addRecordDlg.Destroy()

        elif action == "deleteLine":
            # -> delete selected vector features
            if self.digit.DeleteSelectedLines() < 0:
                return
            self._updateATM()
        elif action == "deleteArea":
            # -> delete selected vector areas
            if self.digit.DeleteSelectedAreas() < 0:
                return
            self._updateATM()
        elif action == "splitLine":
            # split line
            if self.digit.SplitLine(self.Pixel2Cell(self.mouse["begin"])) < 0:
                return
        elif action == "addVertex":
            # add vertex
            fid = self.digit.AddVertex(self.Pixel2Cell(self.mouse["begin"]))
            if fid < 0:
                return
        elif action == "removeVertex":
            # remove vertex
            fid = self.digit.RemoveVertex(self.Pixel2Cell(self.mouse["begin"]))
            if fid < 0:
                return
            self._geomAttrbUpdate(
                [
                    fid,
                ]
            )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9c2b3b51c8 (style(gui): Fixes literal-membership (PLR6201) (#3952))
        elif action in {"copyCats", "copyAttrs"} and hasattr(self, "copyCatsIds"):
=======
        elif action in ("copyCats", "copyAttrs") and hasattr(self, "copyCatsIds"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        elif action in ("copyCats", "copyAttrs") and hasattr(self, "copyCatsIds"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        elif action in {"copyCats", "copyAttrs"} and hasattr(self, "copyCatsIds"):
>>>>>>> 6bd0f720cb (style(gui): Fixes literal-membership (PLR6201) (#3952))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        elif action in ("copyCats", "copyAttrs") and hasattr(self, "copyCatsIds"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9c2b3b51c8 (style(gui): Fixes literal-membership (PLR6201) (#3952))
            if action == "copyCats":
                if (
                    self.digit.CopyCats(
                        self.copyCatsList, self.copyCatsIds, copyAttrb=False
                    )
                    < 0
                ):
                    return
            elif (
                self.digit.CopyCats(self.copyCatsList, self.copyCatsIds, copyAttrb=True)
                < 0
            ):
                return

            del self.copyCatsList
            del self.copyCatsIds

            self._updateATM()

        elif action == "editLine" and hasattr(self, "moveInfo"):
            line = self.digit.GetDisplay().GetSelected()[0]
            if self.digit.EditLine(line, self.polycoords) < 0:
                return

            del self.moveInfo

        elif action == "flipLine":
            if self.digit.FlipLine() < 0:
                return
        elif action == "mergeLine":
            if self.digit.MergeLine() < 0:
                return
        elif action == "breakLine":
            if self.digit.BreakLine() < 0:
                return
        elif action == "snapLine":
            if self.digit.SnapLine() < 0:
                return
        elif action == "connectLine":
            if len(self.digit.GetDisplay().GetSelected()) > 1:
                if self.digit.ConnectLine() < 0:
                    return
        elif action == "copyLine":
            if self.digit.CopyLine(self.copyIds) < 0:
                return
            del self.copyIds
            if self.layerTmp:
                self.Map.DeleteLayer(self.layerTmp)
                self.UpdateMap(render=True, renderVector=False)
            del self.layerTmp

        elif action == "zbulkLine" and len(self.polycoords) == 2:
            pos1 = self.polycoords[0]
            pos2 = self.polycoords[1]

            selected = self.digit.GetDisplay().GetSelected()
            dlg = VDigitZBulkDialog(
                parent=self, title=_("Z bulk-labeling dialog"), nselected=len(selected)
            )
            if dlg.ShowModal() == wx.ID_OK:
                if (
                    self.digit.ZBulkLines(
                        pos1, pos2, dlg.value.GetValue(), dlg.step.GetValue()
                    )
                    < 0
                ):
                    return
            self.UpdateMap(render=False)
        elif action == "typeConv":
            # -> feature type conversion
            # - point <-> centroid
            # - line <-> boundary
            if self.digit.TypeConvForSelectedLines() < 0:
                return

        if action != "addLine":
            # unselect and re-render
            self.digit.GetDisplay().SetSelected([])
            self.polycoords = []
            self.UpdateMap(render=False)

    def _onMouseMoving(self, event):
        self.mouse["end"] = event.GetPosition()

        Debug.msg(
            5,
            "VDigitWindow.OnMouseMoving(): coords=%f,%f"
            % (self.mouse["end"][0], self.mouse["end"][1]),
        )

        action = self.toolbar.GetAction()
        if action == "addLine" and self.toolbar.GetAction("type") in {
            "line",
            "boundary",
            "area",
        }:
            if len(self.polycoords) > 0:
                self.MouseDraw(
                    pdc=self.pdcTmp, begin=self.Cell2Pixel(self.polycoords[-1])
                )

        elif action in {"moveLine", "moveVertex", "editLine"} and hasattr(
            self, "moveInfo"
        ):
            dx = self.mouse["end"][0] - self.mouse["begin"][0]
            dy = self.mouse["end"][1] - self.mouse["begin"][1]

            # draw lines on new position
            if action == "moveLine" and len(self.moveInfo["id"]) > 0:
                # move line
                for id in self.moveInfo["id"]:
                    self.pdcTmp.TranslateId(id, dx, dy)
            elif action in {"moveVertex", "editLine"}:
                # move vertex ->
                # (vertex, left vertex, left line,
                # right vertex, right line)

                # do not draw static lines
                if action == "moveVertex" and len(self.moveInfo["id"]) > 0:
                    self.polycoords = []
                    self.pdcTmp.RemoveId(self.moveInfo["id"][0])
                    if self.moveInfo["id"][1] > 0:  # previous vertex
                        x, y = self.Pixel2Cell(
                            self.pdcTmp.GetIdBounds(self.moveInfo["id"][1])[0:2]
                        )
                        self.pdcTmp.RemoveId(self.moveInfo["id"][1] + 1)
                        self.polycoords.append((x, y))
                    self.polycoords.append(self.Pixel2Cell(self.mouse["end"]))

                    if self.moveInfo["id"][2] > 0:  # next vertex
                        x, y = self.Pixel2Cell(
                            self.pdcTmp.GetIdBounds(self.moveInfo["id"][2])[0:2]
                        )
                        self.pdcTmp.RemoveId(self.moveInfo["id"][2] - 1)
                        self.polycoords.append((x, y))

                    self.ClearLines(pdc=self.pdcTmp)
                    self.DrawLines(pdc=self.pdcTmp)

                if action == "editLine":
                    if self.polycoords:
                        self.MouseDraw(
                            pdc=self.pdcTmp, begin=self.Cell2Pixel(self.polycoords[-1])
                        )

            self.Refresh()  # TODO: use RefreshRect()
            self.mouse["begin"] = self.mouse["end"]

        elif action == "zbulkLine":
            if len(self.polycoords) == 1:
                # draw mouse moving
                self.MouseDraw(self.pdcTmp)

    def _zoom(self, event):
        tmp1 = self.mouse["end"]
        tmp2 = self.Cell2Pixel(self.moveInfo["begin"])
        dx = tmp1[0] - tmp2[0]
        dy = tmp1[1] - tmp2[1]
        self.moveInfo["beginDiff"] = (dx, dy)
        for id in self.moveInfo["id"]:
            self.pdcTmp.RemoveId(id)

    def _addRecord(self):
        return UserSettings.Get(group="vdigit", key="addRecord", subkey="enabled")
