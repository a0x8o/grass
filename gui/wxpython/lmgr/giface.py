"""
@package lmgr.giface

@brief Layer Manager GRASS interface

Classes:
 - giface::LayerManagerGrassInterface

(C) 2012 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Anna Kratochvilova <kratochanna gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com>
"""

from grass.pydispatch.signal import Signal
from core.giface import Notification
from core.utils import GetLayerNameFromCmd


class Layer:
    """@implements core::giface::Layer

    .. note::

        Currently implemented without specifying the interface.
        It only provides all attributes of existing layer as used in lmgr.
    """

    def __init__(self, layer, pydata):
        self._layer = layer
        self._pydata = pydata

    def __getattr__(self, name):
        return self._pydata[0][name]

    def __dir__(self):
        return self._pydata[0].keys()

    def __str__(self):
        return (
            ""
            if (self.maplayer is None or self.maplayer.name is None)
            else self.maplayer.name
        )


class LayerList:
    """@implements core.giface.Layer"""

    def __init__(self, tree):
        self._tree = tree

    def __len__(self):
        # The list constructor calls __len__ as an optimization if available,
        # causing a RecursionError
        return len([layer for layer in self])  # noqa: C416

    def __iter__(self):
        """Iterates over the contents of the list."""
        if self._tree:
            item = self._tree.GetFirstChild(self._tree.root)[0]
            while item and item.IsOk():
                yield Layer(item, self._tree.GetPyData(item))
                item = self._tree.GetNextItem(item)

    def __getitem__(self, index):
        """Select a layer from the LayerList using the index."""
<<<<<<< HEAD
        return list(self)[index]
=======
        return [layer for layer in self][index]
>>>>>>> ba65a804c6 (Checks: fix flake8 E741 in gui/wxpython directory (#3926))

    def __repr__(self):
        """Return a representation of the object."""
        return "LayerList(%r)" % list(self)

    def GetSelectedLayers(self, checkedOnly=True):
        items = self._tree.GetSelectedLayer(multi=True, checkedOnly=checkedOnly)
        layers = []
        for item in items:
            layer = Layer(item, self._tree.GetPyData(item))
            layers.append(layer)
        return layers

    # TODO: it is not clear if default of checkedOnly should be False or True
    def GetSelectedLayer(self, checkedOnly=False):
        """Returns selected layer or None when there is no selected layer."""
        item = self._tree.GetSelectedLayer(multi=False, checkedOnly=checkedOnly)
        if item is None:
            return None
        data = self._tree.GetPyData(item)
        return Layer(item, data)

    def GetLayerInfo(self, layer):
        """For compatibility only, will be removed."""
        return Layer(layer, self._tree.GetPyData(layer))

    def AddLayer(self, ltype, name=None, checked=None, opacity=1.0, cmd=None):
        """Adds a new layer to the layer list.

        Launches property dialog if needed (raster, vector, etc.)

        :param ltype: layer type (raster, vector, raster_3d, ...)
        :param name: layer name
        :param checked: if True layer is checked
        :param opacity: layer opacity level
        :param cmd: command (given as a list)
        """
        new_layer_lst = self._tree.AddLayer(
            ltype=ltype, lname=name, lchecked=checked, lopacity=opacity, lcmd=cmd
        )
        return Layer(new_layer_lst, self._tree.GetPyData(new_layer_lst))

    def DeleteLayer(self, layer):
        """Remove layer from layer list"""
        self._tree.Delete(layer._layer)

    def CheckLayer(self, layer, checked=True):
        """Check or uncheck layer"""
        self._tree.forceCheck = True
        self._tree.CheckItem(layer._layer, checked=checked)

    def SelectLayer(self, layer, select=True):
        "Select or unselect layer"
        self._tree.SelectItem(layer._layer, select)

    def ChangeLayer(self, layer, **kwargs):
        "Change layer (cmd, ltype, opacity)"
        if "cmd" in kwargs:
            layer._pydata[0]["cmd"] = kwargs["cmd"]
            layerName, found = GetLayerNameFromCmd(kwargs["cmd"], fullyQualified=True)
            if found:
                layer._pydata[0]["label"] = layerName
        if "ltype" in kwargs:
            layer._pydata[0]["type"] = kwargs["ltype"]
        if "opacity" in kwargs:
            layer._pydata[0]["maplayer"].SetOpacity(kwargs["opacity"])

        self._tree.ChangeLayer(layer._layer)
        self._tree.SetItemIcon(layer._layer)
        self._tree.SetItemText(layer._layer, self._tree._getLayerName(layer._layer))

    def IsLayerChecked(self, layer):
        """Returns True if layer is checked, False otherwise"""
        return self._tree.IsItemChecked(layer._layer)

    def GetLayersByName(self, name):
        items = self._tree.FindItemByData(key="name", value=name)
        if items is None:
            return []
        layers = []
        for item in items:
            layer = Layer(item, self._tree.GetPyData(item))
            layers.append(layer)
        return layers

    def GetLayerByData(self, key, value):
        """Returns layer with specified.

        Returns only one layer.
        Avoid using this method, it might be removed in the future.
        """
        if key == "name":
            print(
                "giface.GetLayerByData(): Do not with use key='name',"
                " use GetLayersByName instead."
            )
        item = self._tree.FindItemByData(key=key, value=value)
        if item is None:
            return None
        return Layer(item, self._tree.GetPyData(item))


class LayerManagerGrassInterface:
    """@implements core::giface::GrassInterface"""

    def __init__(self, lmgr):
        """Constructor is specific to the current implementation.

        Uses Layer Manager object including its private attributes.
        (It encapsulates existing Layer Manager so access to private members
        is intention.)
        """
        self.lmgr = lmgr

        # Signal when some map is created or updated by a module.
        # Used for adding/refreshing displayed layers.
        # attributes: name: map name, ltype: map type,
        # add: if map should be added to layer tree (questionable attribute)
        self.mapCreated = Signal("LayerManagerGrassInterface.mapCreated")

        # Signal for communicating current mapset has been switched
        self.currentMapsetChanged = Signal(
            "LayerManagerGrassInterface.currentMapsetChanged"
        )

        # Signal for communicating something in current grassdb has changed.
        # Parameters:
        # action: required, is one of 'new', 'rename', 'delete'
        # element: required, can be one of 'grassdb', 'location', 'mapset', 'raster',
        #          'vector' and 'raster_3d'
        # grassdb: path to grass db, required
        # location: location name, required
        # mapset: mapset name, required when element is 'mapset', 'raster',
        #         'vector' or 'raster_3d'
        # map: map name, required when element is 'raster', 'vector' or 'raster_3d'
        # newname: new name (of mapset, map), required with action='rename'
        self.grassdbChanged = Signal("LayerManagerGrassInterface.grassdbChanged")

        # Signal emitted to request updating of map
        self.updateMap = Signal("LayerManagerGrassInterface.updateMap")

        # Signal emitted when workspace is changed
        self.workspaceChanged = Signal("LayerManagerGrassInterface.workspaceChanged")

        # Signal emitted when entry to history is added
        self.entryToHistoryAdded = Signal(
            "LayerManagerGrassInterface.entryToHistoryAdded"
        )

        # Signal emitted when entry from history is removed
        self.entryFromHistoryRemoved = Signal(
            "LayerManagerGrassInterface.entryFromHistoryRemoved"
        )

        # Signal emitted when entry in history is updated
        self.entryInHistoryUpdated = Signal(
            "LayerManagerGrassInterface.entryInHistoryUpdated"
        )

    def RunCmd(self, *args, **kwargs):
        self.lmgr._gconsole.RunCmd(*args, **kwargs)

    def Help(self, entry, online=False):
        cmdlist = ["g.manual", "entry=%s" % entry]
        if online:
            cmdlist.append("-o")
        self.RunCmd(cmdlist, compReg=False, notification=Notification.NO_NOTIFICATION)

    def WriteLog(self, text, wrap=None, notification=Notification.HIGHLIGHT):
        self.lmgr._gconsole.WriteLog(text=text, wrap=wrap, notification=notification)

    def WriteCmdLog(self, text, pid=None, notification=Notification.MAKE_VISIBLE):
        self.lmgr._gconsole.WriteCmdLog(text=text, pid=pid, notification=notification)

    def WriteWarning(self, text):
        self.lmgr._gconsole.WriteWarning(text=text)

    def WriteError(self, text):
        self.lmgr._gconsole.WriteError(text=text)

    def GetLog(self, err=False):
        return self.lmgr._gconsole.GetLog(err=err)

    def GetLayerTree(self):
        return self.lmgr.GetLayerTree()

    def GetLayerList(self):
        return LayerList(self.lmgr.GetLayerTree())

    def GetMapDisplay(self):
        return self.lmgr.GetMapDisplay(onlyCurrent=True)

    def GetAllMapDisplays(self):
        return self.lmgr.GetMapDisplay(onlyCurrent=False)

    def GetMapWindow(self):
        if self.lmgr.GetMapDisplay(onlyCurrent=True):
            return self.lmgr.GetMapDisplay(onlyCurrent=True).GetMapWindow()
        return None

    def GetProgress(self):
        return self.lmgr.goutput.GetProgressBar()


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
class LayerManagerGrassInterfaceForMapDisplay:
=======
    def ShowStatusbar(self, show=True):
        self.lmgr.GetMapDisplay().ShowStatusbar(show)

    def IsStatusbarShown(self):
        return self.lmgr.GetMapDisplay().IsStatusbarShown()

    def ShowAllToolbars(self, show=True):
        if not show:  # hide
            action = self.lmgr.GetMapDisplay().RemoveToolbar
        else:
            action = self.lmgr.GetMapDisplay().AddToolbar
        for toolbar in self.lmgr.GetMapDisplay().GetToolbarNames():
            action(toolbar)

    def AreAllToolbarsShown(self):
        return self.lmgr.GetMapDisplay().GetMapToolbar().IsShown()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
=======
=======
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 504a46451c (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 4e96c0c0e8 (libpython: Save and load benchmark results (#1711))
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 86e790785c (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 1906f4a791 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 476ef44553 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 345367a7c1 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 4b334d121f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 56976800a2 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f2dfa9a433 (libpython: Save and load benchmark results (#1711))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> de5b9cd94f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 2bf163e4b3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> fb4ab822d8 (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> aa15e7c6e3 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> d56ffd79c6 (libpython: Save and load benchmark results (#1711))
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
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
>>>>>>> 8d53b00588 (libpython: Save and load benchmark results (#1711))
>>>>>>> f8d32d9e3a (libpython: Save and load benchmark results (#1711))

class LayerManagerGrassInterfaceForMapDisplay(object):
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
    """Provides reference only to the given layer list (according to tree),
    not to the current.

    @implements core::giface::GrassInterface
    """

    def __init__(self, giface, tree):
        """
        :param giface: original grass interface
        :param tree: tree which will be used instead of the tree from giface
        """
        self._giface = giface
        self.tree = tree

        # Signal emitted to request updating of map
        self.updateMap = Signal("LayerManagerGrassInterfaceForMapDisplay.updateMap")

    def GetLayerTree(self):
        return self.tree

    def GetLayerList(self):
        return LayerList(self.tree)

    def GetMapWindow(self):
        return self.tree.GetMapDisplay().GetMapWindow()

    def __getattr__(self, name):
        return getattr(self._giface, name)
