"""GRASS GIS interface to Python exceptions
"""

import subprocess


class DBError(Exception):
    pass


class FatalError(Exception):
    pass


class FlagError(Exception):
    pass


class GrassError(Exception):
    pass


class ImplementationError(Exception):
    pass


class OpenError(Exception):
    pass


class ParameterError(Exception):
    pass


class ScriptError(Exception):
    """Raised during script execution. ::

    >>> error = ScriptError('My error message!')
    >>> error.value
    'My error message!'
    >>> print(error)
    My error message!
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Usage(Exception):
    pass


# TODO: we inherit from subprocess to be aligned with check_call but it is needed?
# perhaps it would be better to inherit from Exception or from ScriptError
class CalledModuleError(subprocess.CalledProcessError):
    """Raised when a called module ends with error (non-zero return code)

    Used for failures of modules called as subprocesses from Python code.
    """

    def __init__(self, module, code, returncode, errors=None):
        """Create an exception with a full error message based on the parameters.

        :param module: module name
        :param code: some code snipped which contains parameters
        :param returncode: process returncode (assuming non-zero)
        :param errors: errors provided by the module (e.g., stderr)
        """
        # CalledProcessError has undocumented constructor
<<<<<<< HEAD
        super().__init__(returncode, module)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> f008e4ec0d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
        # No need to include module name if it is directly in code of if it is not set.
        # Otherwise, make sure module name is there if provided and not in code.
        executed = code if not module or module in code else f"{module} {code}"
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 628e5dfc04 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> c190252548 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae94629933 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> d08c50382a (pythonlib: Remove star imports (#1546))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
=======
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 27551073cd (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ae94629933 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2f785ecbac (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f008e4ec0d (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 9441e85caa (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a0e50c9b34 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ba719f126c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8fcf52b064 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e2d3096606 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2bb9b85a2d (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> ba3eb01af9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 1acc93c650 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> e1a7453c89 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 158dbc71ea (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> c6554e4c24 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8ac6037718 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
>>>>>>> 3960f36bc5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> d08c50382a (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0bd7d818a8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 8630c1908e (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 5fb05831cc (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 6fdaa03757 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bdc1a9eff8 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> e54d3f3e40 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 56010eb999 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 692afe97f6 (pythonlib: Remove star imports (#1546))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> 240dcc86f4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 65eebf45c4 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 705f9aa694 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ab33fc0b6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2ec038aafa (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 78a24c3407 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bd15a01a37 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 858dcd2c02 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
>>>>>>> 1df4f6c1a9 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> b62c64d69c (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> a7c34931b5 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 2e4a058ca6 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fa4b4b8fe (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fcbc6eaf1c (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 0b441b6432 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 958298688f (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 0915ba12ad (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> db4f0c5e9e (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 474e98d46c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> edbe88c194 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 4fbbce42f6 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 7c9ebb33c7 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 4bd0126b6c (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> fd6b673316 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> dd23d5dc15 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> bf337dfc4c (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9e2a78d963 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 9407a0d6c1 (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> e397082cd0 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f8a1d36c40 (pythonlib: Remove star imports (#1546))
=======
=======
=======
        super(CalledModuleError, self).__init__(returncode, module)
<<<<<<< HEAD
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> f4b9197871 (pythonlib: Remove star imports (#1546))
<<<<<<< HEAD
>>>>>>> 38eafe025f (pythonlib: Remove star imports (#1546))
=======
=======
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
>>>>>>> 3ced907ea6 (pythonlib: Remove star imports (#1546))
>>>>>>> 9cb1837c15 (pythonlib: Remove star imports (#1546))
        if not module or module in code:
            # No need to include module name if it is directly in code
            # of if it is not set.
            executed = code
        else:
            # Make sure module name is there if provided and not in code.
            executed = f"{module} {code}"
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ce79f96bcb (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 3fce2ed438 (pythonlib: Remove star imports (#1546))
=======
>>>>>>> 7e8f036e2d (pythonlib: Remove star imports (#1546))
        if errors:
            # We assume actual errors, e.g., captured stderr.
            err = _("See the following errors:\n{errors}").format(errors=errors)
        else:
            # In command line, the errors will be above, but in testing framework
            # or notebooks, the errors will be somewhere else than the traceback.
            err = _("See errors above the traceback or in the error output.")
        # The full message
        self.msg = _(
            "Module run `{executed}` ended with an error.\n"
            "The subprocess ended with a non-zero return code: {returncode}."
            " {see_errors}"
        ).format(
            executed=executed,
            returncode=returncode,
            see_errors=err,
        )

    def __str__(self):
        return self.msg
