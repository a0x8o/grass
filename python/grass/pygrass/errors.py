from functools import wraps

from grass.exceptions import GrassError

from grass.pygrass.messages import get_msgr
import grass.lib.gis as libgis


def must_be_open(method):
    @wraps(method)
    def wrapper(self, *args, **kargs):
        if self.is_open():
            return method(self, *args, **kargs)
        msgr = get_msgr()
        msgr.warning(_("The map is close!"))

    return wrapper


def mapinfo_must_be_set(method):
    @wraps(method)
    def wrapper(self, *args, **kargs):
        if self.c_mapinfo:
            return method(self, *args, **kargs)
<<<<<<< HEAD
        raise GrassError(_("The self.c_mapinfo pointer must be correctly initiated"))
=======
        else:
            raise GrassError(
                _("The self.c_mapinfo pointer must be correctly initiated")
            )
>>>>>>> fb2b1e4ce2 (style: Fix single-line-implicit-string-concatenation violations (ISC001)  (#3943))

    return wrapper


def must_be_in_current_mapset(method):
    @wraps(method)
    def wrapper(self, *args, **kargs):
        if self.mapset == libgis.G_mapset().decode():
            return method(self, *args, **kargs)
        raise GrassError(_("Map <{}> not found in current mapset").format(self.name))

    return wrapper
