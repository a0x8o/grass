"""
@package lmgr.toolbars

@brief wxGUI Layer Manager - toolbars

Classes:
 - toolbars::LMWorkspaceToolbar
 - toolbars::DisplayPanelToolbar
 - toolbars::LMToolsToolbar
 - toolbars::LMMiscToolbar
 - toolbars::LMNvizToolbar


(C) 2007-2013 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.

@author Michael Barton
@author Jachym Cepicky
@author Martin Landa <landa.martin gmail.com>
@author Anna Kratochvilova <kratochanna gmail.com>
@author Linda Kladivova <linda.kladivova gmail com>
"""

from core.gcmd import RunCommand
from gui_core.toolbars import BaseToolbar, AuiToolbar, BaseIcons
from icons.icon import MetaIcon


class LMWorkspaceToolbar(AuiToolbar):
    """Layer Manager `workspace` toolbar"""

    def __init__(self, parent):
        AuiToolbar.__init__(self, parent)

        self.InitToolbar(self._toolbarData())

        # realize the toolbar
        self.Realize()

    def _toolbarData(self):
        """Toolbar data"""
        icons = {
            "workspaceNew": MetaIcon(
                img="create", label=_("Create new workspace (Ctrl+N)")
            ),
            "workspaceOpen": MetaIcon(
                img="open", label=_("Open existing workspace file (Ctrl+O)")
            ),
            "workspaceSave": MetaIcon(
                img="save", label=_("Save current workspace to file (Ctrl+S)")
            ),
        }
        return self._getToolbarData(
            (
                (
                    ("workspaceNew", _("New workspace")),
                    icons["workspaceNew"],
                    self.parent.OnWorkspaceNew,
                ),
                (
                    ("workspaceOpen", _("Open workspace")),
                    icons["workspaceOpen"],
                    self.parent.OnWorkspaceOpen,
                ),
                (
                    ("workspaceSave", _("Save workspace")),
                    icons["workspaceSave"],
                    self.parent.OnWorkspaceSave,
                ),
            )
        )


class DisplayPanelToolbar(BaseToolbar):
    """Toolbar for display tab"""

    def __init__(self, guiparent, parent):
        BaseToolbar.__init__(self, guiparent)
        self.parent = parent

        self.InitToolbar(self._toolbarData())

        # realize the toolbar
        self.Realize()

    def _toolbarData(self):
        """Toolbar data"""
        icons = {
            "addMulti": MetaIcon(
                img="layer-open",
                label=_("Add multiple raster or vector map layers (Ctrl+Shift+L)"),
            ),
            "addRast": BaseIcons["addRast"].SetLabel(
                _("Add raster map layer (Ctrl+Shift+R)")
            ),
            "rastMisc": MetaIcon(
                img="layer-raster-more",
                label=_("Add various raster map layers (RGB, HIS, shaded relief...)"),
            ),
            "addVect": BaseIcons["addVect"].SetLabel(
                _("Add vector map layer (Ctrl+Shift+V)")
            ),
            "vectMisc": MetaIcon(
                img="layer-vector-more",
                label=_("Add various vector map layers (thematic, chart...)"),
            ),
            "addWS": MetaIcon(
                img="layer-wms-add",
                label=_("Add web service layer (WMS, WMTS, NASA OnEarth)"),
            ),
            "addGroup": MetaIcon(img="layer-group-add", label=_("Add group")),
            "addOverlay": MetaIcon(img="layer-more", label=_("Add various overlays")),
            "delCmd": MetaIcon(
                img="layer-remove",
                label=_("Remove selected map layer(s) from layer tree"),
            ),
            "vdigit": MetaIcon(img="edit", label=_("Edit selected vector map")),
            "attrTable": MetaIcon(
                img="table", label=_("Show attribute data for selected vector map")
            ),
        }

        return self._getToolbarData(
            (
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                (
                    ("addMulti", _("Add multiple map layers")),
                    icons["addMulti"],
                    self.parent.OnAddMaps,
                ),
                (
                    ("addrast", _("Add raster map")),
                    icons["addRast"],
                    self.parent.OnAddRaster,
                ),
                (
                    ("rastmisc", _("Add various raster maps")),
                    icons["rastMisc"],
                    self.parent.OnAddRasterMisc,
                ),
                (
                    ("addvect", _("Add vector map")),
                    icons["addVect"],
                    self.parent.OnAddVector,
                ),
                (
                    ("vectmisc", _("Add various vector maps")),
                    icons["vectMisc"],
                    self.parent.OnAddVectorMisc,
                ),
                (
                    ("addovl", _("Add various overlays")),
                    icons["addOverlay"],
                    self.parent.OnAddOverlay,
                ),
                (
                    ("addWS", _("Add web service map")),
                    icons["addWS"],
                    self.parent.OnAddWS,
                ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                (None,),
                (
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> main
=======
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
                (None,),
                (
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
<<<<<<< HEAD
=======
                ("addMulti", icons["addMulti"], self.parent.OnAddMaps),
                ("addrast", icons["addRast"], self.parent.OnAddRaster),
                ("rastmisc", icons["rastMisc"], self.parent.OnAddRasterMisc),
                ("addvect", icons["addVect"], self.parent.OnAddVector),
                ("vectmisc", icons["vectMisc"], self.parent.OnAddVectorMisc),
                ("addovl", icons["addOverlay"], self.parent.OnAddOverlay),
                ("addWS", icons["addWS"], self.parent.OnAddWS),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                (None,),
                (
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
                    ("addgrp", icons["addGroup"].label),
                    icons["addGroup"],
                    self.parent.OnAddGroup,
                ),
                (
                    ("delcmd", _("Delete map layer")),
                    icons["delCmd"],
                    self.parent.OnDeleteLayer,
                ),
                (None,),
                (
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                (None,),
                (
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                    ("vdigit", icons["vdigit"].label),
                    icons["vdigit"],
                    self.parent.OnVDigit,
                ),
                (
                    ("attribute", icons["attrTable"].label),
                    icons["attrTable"],
                    self.parent.OnShowAttributeTable,
                ),
            )
        )


class LMToolsToolbar(AuiToolbar):
    """Layer Manager `tools` toolbar"""

    def __init__(self, parent):
        AuiToolbar.__init__(self, parent)

        self.InitToolbar(self._toolbarData())

        # realize the toolbar
        self.Realize()

    def _toolbarData(self):
        """Toolbar data"""
        icons = {
            "newdisplay": MetaIcon(
                img="monitor-create", label=_("Start new map display")
            ),
            "mapcalc": MetaIcon(
                img="raster-calculator", label=_("Raster Map Calculator")
            ),
            "modeler": MetaIcon(img="modeler-main", label=_("Graphical Modeler")),
            "georectify": MetaIcon(img="georectify", label=_("Georectifier")),
            "composer": MetaIcon(img="print-compose", label=_("Cartographic Composer")),
            "script-load": MetaIcon(
                img="script-load", label=_("Launch user-defined script")
            ),
            "python": MetaIcon(
                img="python", label=_("Open a simple Python code editor")
            ),
        }

        return self._getToolbarData(
            (
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                (
                    ("newdisplay", _("New display")),
                    icons["newdisplay"],
                    self.parent.OnNewDisplay,
                ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> bfcba1482b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
                ("newdisplay", icons["newdisplay"], self.parent.OnNewDisplay),
                (None,),
                ("mapCalc", icons["mapcalc"], self.parent.OnMapCalculator),
                ("georect", icons["georectify"], self.parent.OnGCPManager),
                ("modeler", icons["modeler"], self.parent.OnGModeler),
                ("mapOutput", icons["composer"], self.parent.OnPsMap),
>>>>>>> 7896e1a53f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> ee253be79a (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 861dec1bf2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f9daf13560 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c6a412e10d (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> c5bad555b2 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8472b7b824 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> da35d0e56f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> d0f7fb7e37 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> f60d41cfac (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2a3f5af732 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> a3f08c4c56 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7ac7d0e0a6 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 6c3db39bfa (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 83bcaf56ef (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 43b862a006 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 99226d09d7 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 86cfd7a703 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 0fec5bf578 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 165e1d768b (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> e60bc7f2ae (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d4beced40f (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
<<<<<<< HEAD
>>>>>>> 145c1c3f72 (wxGUI/Single-Window: New change page event for AuiNotebook (#1780))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("mapCalc", icons["mapcalc"].label),
                    icons["mapcalc"],
                    self.parent.OnMapCalculator,
                ),
                (
                    ("georect", icons["georectify"].label),
                    icons["georectify"],
                    self.parent.OnGCPManager,
                ),
                (
                    ("modeler", icons["modeler"].label),
                    icons["modeler"],
                    self.parent.OnGModeler,
                ),
                (
                    ("mapOutput", icons["composer"].label),
                    icons["composer"],
                    self.parent.OnPsMap,
                ),
                (None,),
                (
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
                (None,),
                (
                    ("mapCalc", icons["mapcalc"].label),
                    icons["mapcalc"],
                    self.parent.OnMapCalculator,
                ),
                (
                    ("georect", icons["georectify"].label),
                    icons["georectify"],
                    self.parent.OnGCPManager,
                ),
                (
                    ("modeler", icons["modeler"].label),
                    icons["modeler"],
                    self.parent.OnGModeler,
                ),
                (
                    ("mapOutput", icons["composer"].label),
                    icons["composer"],
                    self.parent.OnPsMap,
                ),
                (None,),
                (
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
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("mapCalc", icons["mapcalc"].label),
                    icons["mapcalc"],
                    self.parent.OnMapCalculator,
                ),
                (
                    ("georect", icons["georectify"].label),
                    icons["georectify"],
                    self.parent.OnGCPManager,
                ),
                (
                    ("modeler", icons["modeler"].label),
                    icons["modeler"],
                    self.parent.OnGModeler,
                ),
                (
                    ("mapOutput", icons["composer"].label),
                    icons["composer"],
                    self.parent.OnPsMap,
                ),
                (None,),
                (
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
                (None,),
                (
                    ("mapCalc", icons["mapcalc"].label),
                    icons["mapcalc"],
                    self.parent.OnMapCalculator,
                ),
                (
                    ("georect", icons["georectify"].label),
                    icons["georectify"],
                    self.parent.OnGCPManager,
                ),
                (
                    ("modeler", icons["modeler"].label),
                    icons["modeler"],
                    self.parent.OnGModeler,
                ),
                (
                    ("mapOutput", icons["composer"].label),
                    icons["composer"],
                    self.parent.OnPsMap,
                ),
                (None,),
                (
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                    ("script-load", icons["script-load"].label),
                    icons["script-load"],
                    self.parent.OnRunScript,
                ),
                (
                    ("python", _("Python code editor")),
                    icons["python"],
                    self.parent.OnSimpleEditor,
                ),
            )
        )


class LMMiscToolbar(AuiToolbar):
    """Layer Manager `misc` toolbar"""

    def __init__(self, parent):
        AuiToolbar.__init__(self, parent)

        self.InitToolbar(self._toolbarData())

        # realize the toolbar
        self.Realize()

    def _toolbarData(self):
        """Toolbar data"""
        icons = {
            "settings": BaseIcons["settings"].SetLabel(_("GUI settings")),
            "help": BaseIcons["help"].SetLabel(_("GRASS manual")),
        }

        return self._getToolbarData(
            (
                (
                    ("settings", icons["settings"].label),
                    icons["settings"],
                    self.parent.OnPreferences,
                ),
                (
                    ("help", icons["help"].label),
                    icons["help"],
                    self.parent.OnHelp,
                ),
            )
        )


class LMNvizToolbar(AuiToolbar):
    """Nviz toolbar"""

    def __init__(self, parent):
        self.lmgr = parent

        AuiToolbar.__init__(self, parent)

        # only one dialog can be open
        self.settingsDialog = None

        self.InitToolbar(self._toolbarData())

        # realize the toolbar
        self.Realize()

    def _toolbarData(self):
        """Toolbar data"""
        icons = {
            "cmd": MetaIcon(
                img="script-save",
                label=_("Generate command for m.nviz.image"),
                desc=_("Generate command for m.nviz.image based on current state"),
            ),
            "settings": MetaIcon(
                img="3d-settings",
                label=_("3D view mode settings"),
                desc=_("Show 3D view mode settings dialog"),
            ),
            "help": MetaIcon(img="3d-help", label=_("Show 3D view mode manual")),
        }

        return self._getToolbarData(
            (
                (
                    ("nvizCmd", icons["cmd"].label),
                    icons["cmd"],
                    self.OnNvizCmd,
                ),
                (None,),
                (
                    ("settings", icons["settings"].label),
                    icons["settings"],
                    self.parent.OnNvizPreferences,
                ),
                (
                    ("help", icons["help"].label),
                    icons["help"],
                    self.OnHelp,
                ),
            )
        )

    def OnNvizCmd(self, event):
        """Show m.nviz.image command"""
        self.lmgr.GetLayerTree().GetMapDisplay().GetWindow().OnNvizCmd()

    def OnHelp(self, event):
        """Show 3D view mode help"""
        if not self.lmgr:
            RunCommand("g.manual", entry="wxGUI.nviz")
        else:
            log = self.lmgr.GetLogWindow()
            log.RunCmd(["g.manual", "entry=wxGUI.nviz"])
