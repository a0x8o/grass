"""
@package mapwin.mapwindow

@brief Map display canvas basic functionality - base class and properties.

Classes:
 - mapwindow::MapWindowProperties
 - mapwindow::MapWindowBase

(C) 2006-2012 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Martin Landa <landa.martin gmail.com>
@author Michael Barton
@author Jachym Cepicky
@author Vaclav Petras <wenzeslaus gmail.com> (handlers support)
@author Stepan Turek <stepan.turek seznam.cz> (handlers support)
"""

import wx

from core.settings import UserSettings
from core.gcmd import GError
from gui_core.wrap import StockCursor

from grass.script import core as grass
from grass.pydispatch.signal import Signal


class MapWindowProperties:
    def __init__(self):
        self._resolution = None
        self.resolutionChanged = Signal("MapWindowProperties.resolutionChanged")
        self._autoRender = None
        self.autoRenderChanged = Signal("MapWindowProperties.autoRenderChanged")
        self._showRegion = None
        self.showRegionChanged = Signal("MapWindowProperties.showRegionChanged")
        self._alignExtent = None
        self.alignExtentChanged = Signal("MapWindowProperties.alignExtentChanged")
        self._useDefinedProjection = False
        self.useDefinedProjectionChanged = Signal(
            "MapWindowProperties.useDefinedProjectionChanged"
        )
        self._sbItem = None
        self.sbItemChanged = Signal("MapWindowProperties.sbItemChanged")

    def setValuesFromUserSettings(self):
        """Convenient function to get values from user settings into this object."""
        self._resolution = UserSettings.Get(
            group="display", key="compResolution", subkey="enabled"
        )
        self._autoRender = UserSettings.Get(
            group="display", key="autoRendering", subkey="enabled"
        )
        self._showRegion = False  # in statusbar.py was not from settings
        self._alignExtent = UserSettings.Get(
            group="display", key="alignExtent", subkey="enabled"
        )

    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        if value != self._resolution:
            self._resolution = value
            self.resolutionChanged.emit(value=value)

    @property
    def autoRender(self):
        return self._autoRender

    @autoRender.setter
    def autoRender(self, value):
        if value != self._autoRender:
            self._autoRender = value
            self.autoRenderChanged.emit(value=value)

    @property
    def showRegion(self):
        return self._showRegion

    @showRegion.setter
    def showRegion(self, value):
        if value != self._showRegion:
            self._showRegion = value
            self.showRegionChanged.emit(value=value)

    @property
    def alignExtent(self):
        return self._alignExtent

    @alignExtent.setter
    def alignExtent(self, value):
        if value != self._alignExtent:
            self._alignExtent = value
            self.alignExtentChanged.emit(value=value)

    @property
    def useDefinedProjection(self):
        return self._useDefinedProjection
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

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

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
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
=======
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

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

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

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
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
=======
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
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
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    @useDefinedProjection.setter
    def useDefinedProjection(self, value):
        if value != self._useDefinedProjection:
            self._useDefinedProjection = value
            self.useDefinedProjectionChanged.emit(value=value)

    @property
    def epsg(self):
        return UserSettings.Get(group="projection", key="statusbar", subkey="epsg")

    @property
    def sbItem(self):
        return self._sbItem

    @sbItem.setter
    def sbItem(self, mode):
        if mode != self._sbItem:
            self._sbItem = mode
            self.sbItemChanged.emit(mode=mode)


class MapWindowBase:
    """Abstract map display window class

    Superclass for BufferedWindow class (2D display mode), and GLWindow
    (3D display mode).

    Subclasses have to define
     - _bindMouseEvents method which binds MouseEvent handlers
     - Pixel2Cell
     - Cell2Pixel (if it is possible)
    """

    def __init__(self, parent, giface, Map):
        self.parent = parent
        self.Map = Map
        self._giface = giface

        # Emitted when someone registers as mouse event handler
        self.mouseHandlerRegistered = Signal("MapWindow.mouseHandlerRegistered")
        # Emitted when mouse event handler is unregistered
        self.mouseHandlerUnregistered = Signal("MapWindow.mouseHandlerUnregistered")
        # emitted after double click in pointer mode on legend, text, scalebar
        self.overlayActivated = Signal("MapWindow.overlayActivated")
        # emitted when overlay should be hidden
        self.overlayRemoved = Signal("MapWindow.overlayRemoved")

        # mouse attributes -- position on the screen, begin and end of
        # dragging, and type of drawing
        self.mouse = {
            "begin": [0, 0],  # screen coordinates
            "end": [0, 0],
            "use": "pointer",
            "box": "point",
        }
        # last east, north coordinates, changes on mouse motion
        self.lastEN = None

        # stores overridden cursor
        self._overriddenCursor = None

        # dictionary where event types are stored as keys and lists of
        # handlers for these types as values
        self.handlersContainer = {
            wx.EVT_LEFT_DOWN: [],
            wx.EVT_LEFT_UP: [],
            wx.EVT_LEFT_DCLICK: [],
            wx.EVT_MIDDLE_DOWN: [],
            wx.EVT_MIDDLE_UP: [],
            wx.EVT_MIDDLE_DCLICK: [],
            wx.EVT_RIGHT_DOWN: [],
            wx.EVT_RIGHT_UP: [],
            wx.EVT_RIGHT_DCLICK: [],
            wx.EVT_MOTION: [],
            wx.EVT_ENTER_WINDOW: [],
            wx.EVT_LEAVE_WINDOW: [],
            wx.EVT_MOUSEWHEEL: [],
            wx.EVT_MOUSE_EVENTS: [],
        }

        # available cursors
        self._cursors = {
            "default": StockCursor(cursorId=wx.CURSOR_ARROW),
            "cross": StockCursor(cursorId=wx.CURSOR_CROSS),
            "hand": StockCursor(cursorId=wx.CURSOR_HAND),
            "pencil": StockCursor(cursorId=wx.CURSOR_PENCIL),
            "sizenwse": StockCursor(cursorId=wx.CURSOR_SIZENWSE),
        }

        # default cursor for window is arrow (at least we rely on it here)
        # but we need to define attribute here
        # cannot call SetNamedCursor since it expects the instance
        # to be a wx window, so setting only the attribute
        self._cursor = "default"

        wx.CallAfter(self.InitBinding)

    def __del__(self):
        self.UnregisterAllHandlers()

    def InitBinding(self):
        """Binds helper functions, which calls all handlers
        registered to events with the events
        """
        for ev, handlers in self.handlersContainer.items():
            self.Bind(ev, self.EventTypeHandler(handlers))

    def EventTypeHandler(self, evHandlers):
        return lambda event: self.HandlersCaller(event, evHandlers)

    def HandlersCaller(self, event, handlers):
        """Helper function which calls all handlers registered for
        event
        """
        for handler in handlers:
            try:
                handler(event)
            except:
                handlers.remove(handler)
                GError(
                    parent=self,
                    message=_(
                        "Error occurred during calling of handler: %s \n"
                        "Handler was unregistered."
                    )
                    % handler.__name__,
                )

        event.Skip()

    def RegisterMouseEventHandler(self, event, handler, cursor=None):
        """Binds event handler

        @deprecated This method is deprecated. Use Signals or drawing API
        instead. Signals do not cover all events but new Signals can be added
        when needed consider also adding generic signal. However, more
        interesting and useful is higher level API to create objects, graphics etc.

        Call event.Skip() in handler to allow default processing in MapWindow.

        If any error occurs inside of handler, the handler is removed.

        Before handler is unregistered it is called with
        string value "unregistered" of event parameter.

        ::

            # your class methods
            def OnButton(self, event):
                # current map display's map window
                # expects LayerManager to be the parent
                self.mapwin = self.parent.GetLayerTree().GetMapDisplay().GetWindow()
                if self.mapwin.RegisterEventHandler(
                    wx.EVT_LEFT_DOWN, self.OnMouseAction, "cross"
                ):
                    self.parent.GetLayerTree().GetMapDisplay().Raise()
                else:
                    # handle that you cannot get coordinates

            def OnMouseAction(self, event):
                # get real world coordinates of mouse click
                coor = self.mapwin.Pixel2Cell(event.GetPositionTuple()[:])
                self.text.SetLabel("Coor: " + str(coor))
                self.mapwin.UnregisterMouseEventHandler(
                    wx.EVT_LEFT_DOWN, self.OnMouseAction
                )
                event.Skip()


        Emits mouseHandlerRegistered signal before handler is registered.

        :param event: one of mouse events
        :param handler: function to handle event
        :param cursor: cursor which temporary overrides current cursor

        :return: True if successful
        :return: False if event cannot be bind
        """
        self.mouseHandlerRegistered.emit()
        # inserts handler into list
        for containerEv, handlers in self.handlersContainer.items():
            if event == containerEv:
                handlers.append(handler)

        self.mouse["useBeforeGenericEvent"] = self.mouse["use"]
        self.mouse["use"] = "genericEvent"

        if cursor:
            self._overriddenCursor = self.GetNamedCursor()
            self.SetNamedCursor(cursor)

        return True

    def UnregisterAllHandlers(self):
        """Unregisters all registered handlers

        @deprecated This method is deprecated. Use Signals or drawing API instead.

        Before each handler is unregistered it is called with string
        value "unregistered" of event parameter.
        """
        for handlers in self.handlersContainer.values():
            for handler in handlers:
                try:
                    handler("unregistered")
                    handlers.remove(handler)
                except:
                    GError(
                        parent=self,
                        message=_(
                            "Error occurred during unregistration of handler: %s \n \
                                       Handler was unregistered."
                        )
                        % handler.__name__,
                    )
                    handlers.remove(handler)

    def UnregisterMouseEventHandler(self, event, handler):
        """Unbinds event handler for event

        @deprecated This method is deprecated. Use Signals or drawing API instead.

        Before handler is unregistered it is called with string value
        "unregistered" of event parameter.

        Emits mouseHandlerUnregistered signal after handler is unregistered.

        :param handler: handler to unbind
        :param event: event from which handler will be unbinded

        :return: True if successful
        :return: False if event cannot be unbind
        """
        # removes handler from list
        for containerEv, handlers in self.handlersContainer.items():
            if event != containerEv:
                continue
            try:
                handler("unregistered")
                if handler in handlers:
                    handlers.remove(handler)
                else:
                    grass.warning(
                        _("Handler: %s was not registered") % handler.__name__
                    )
            except:
                GError(
                    parent=self,
                    message=_(
                        "Error occurred during unregistration of handler: %s \n \
                                       Handler was unregistered"
                    )
                    % handler.__name__,
                )
                handlers.remove(handler)

        # restore mouse use (previous state)
        self.mouse["use"] = self.mouse["useBeforeGenericEvent"]

        # restore overridden cursor
        if self._overriddenCursor:
            self.SetNamedCursor(self._overriddenCursor)

        self.mouseHandlerUnregistered.emit()
        return True

    def Pixel2Cell(self, xyCoords):
        raise NotImplementedError

    def Cell2Pixel(self, enCoords):
        raise NotImplementedError

    def OnMotion(self, event):
        """Tracks mouse motion and update statusbar

        .. todo::
            remove this method when lastEN is not used

        :func:`GetLastEN`
        """
        try:
            self.lastEN = self.Pixel2Cell(event.GetPosition())
        except ValueError:
            self.lastEN = None

        event.Skip()

    def GetLastEN(self):
        """Returns last coordinates of mouse cursor.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
        @deprecated This method is deprecated. Use Signal with coordinates as
        parameters.
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
        @deprecated This method is deprecated. Use Signal with coordinates as parameters.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))

        :func:`OnMotion`
        """
        return self.lastEN

    def SetNamedCursor(self, cursorName):
        """Sets cursor defined by name."""
        cursor = self._cursors[cursorName]
        self.SetCursor(cursor)
        self._cursor = cursorName

    def GetNamedCursor(self):
        """Returns current cursor name."""
        return self._cursor

    cursor = property(fget=GetNamedCursor, fset=SetNamedCursor)

    def SetModePointer(self):
        """Sets mouse mode to pointer."""
        self.mouse["use"] = "pointer"
        self.mouse["box"] = "point"
        self.SetNamedCursor("default")

    def SetModePan(self):
        """Sets mouse mode to pan."""
        self.mouse["use"] = "pan"
        self.mouse["box"] = "box"
        self.zoomtype = 0
        self.SetNamedCursor("hand")

    def SetModeZoomIn(self):
        self._setModeZoom(zoomType=1)

    def SetModeZoomOut(self):
        self._setModeZoom(zoomType=-1)

    def _setModeZoom(self, zoomType):
        self.zoomtype = zoomType
        self.mouse["use"] = "zoom"
        self.mouse["box"] = "box"
        self.pen = wx.Pen(colour="Red", width=2, style=wx.SHORT_DASH)
        self.SetNamedCursor("cross")

    def SetModeDrawRegion(self):
        self.mouse["use"] = "drawRegion"
        self.mouse["box"] = "box"
        self.pen = wx.Pen(colour="Red", width=2, style=wx.SHORT_DASH)
        self.SetNamedCursor("cross")

    def SetModeQuery(self):
        """Query mode on"""
        self.mouse["use"] = "query"
        self.mouse["box"] = "point"
        self.zoomtype = 0
        self.SetNamedCursor("cross")

    def DisactivateWin(self):
        """Use when the class instance is hidden in MapFrame."""
        raise NotImplementedError

    def ActivateWin(self):
        """Used when the class instance is activated in MapFrame."""
        raise NotImplementedError
