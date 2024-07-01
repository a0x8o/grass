from grass.pygrass.modules.interface.docstring import docstring_property
from grass.pygrass.modules.interface import read


class Flag:
    """The Flag object store all information about a flag of module.

    It is possible to set flags of command using this object.

    >>> flag = Flag(diz=dict(name='a', description='Flag description',
    ...                      default=True))
    >>> flag.name
    'a'
    >>> flag.special
    False
    >>> flag.description
    'Flag description'
    >>> flag = Flag(diz=dict(name='overwrite'))
    >>> flag.name
    'overwrite'
    >>> flag.special
    True
    """

    def __init__(self, xflag=None, diz=None):
        self.value = False
        diz = read.element2dict(xflag) if xflag is not None else diz
        self.name = diz["name"]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.special = self.name in {"verbose", "overwrite", "quiet", "run"}
=======
<<<<<<< HEAD
<<<<<<< HEAD
        self.special = (
            True if self.name in {"verbose", "overwrite", "quiet", "run"} else False
        )
=======
        self.special = self.name in {"verbose", "overwrite", "quiet", "run"}
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        self.special = self.name in {"verbose", "overwrite", "quiet", "run"}
=======
>>>>>>> 001cfcbd00 (style: Fixes literal-membership (PLR6201) for other code (#3954))
        self.special = (
            True if self.name in {"verbose", "overwrite", "quiet", "run"} else False
        )
>>>>>>> 75456afff2 (style: Fixes literal-membership (PLR6201) for other code (#3954))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d2a8cd08c4 (style: Fixes literal-membership (PLR6201) for other code (#3954))
=======
=======
        self.special = self.name in {"verbose", "overwrite", "quiet", "run"}
>>>>>>> 9a2b1d234a (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
>>>>>>> a2f268d57b (style: Fix if-expr-with-true-false (SIM210) and if-expr-with-false-true (SIM211) (#3999))
=======
>>>>>>> 001cfcbd00 (style: Fixes literal-membership (PLR6201) for other code (#3954))
        self.description = diz.get("description", None)
        self.default = diz.get("default", None)
        self.guisection = diz.get("guisection", None)
        self.suppress_required = "suppress_required" in diz

    def get_bash(self):
        """Return the BASH representation of a flag.

        >>> flag = Flag(diz=dict(name='a', description='Flag description',
        ...                      default=True))
        >>> flag.get_bash()
        ''
        >>> flag.value = True
        >>> flag.get_bash()
        '-a'
        >>> flag = Flag(diz=dict(name='overwrite'))
        >>> flag.get_bash()
        ''
        >>> flag.value = True
        >>> flag.get_bash()
        '--o'
        """
        if self.value:
            if self.special:
                return "--%s" % self.name[0]
            return "-%s" % self.name
        return ""

    def get_python(self):
        """Return the python representation of a flag.

        >>> flag = Flag(diz=dict(name='a', description='Flag description',
        ...                      default=True))
        >>> flag.get_python()
        ''
        >>> flag.value = True
        >>> flag.get_python()
        'a'
        >>> flag = Flag(diz=dict(name='overwrite'))
        >>> flag.get_python()
        ''
        >>> flag.value = True
        >>> flag.get_python()
        'overwrite=True'
        """
        if self.value:
            return "%s=True" % self.name if self.special else self.name
        return ""

    def __str__(self):
        """Return the BASH representation of the flag."""
        return self.get_bash()

    def __repr__(self):
        """Return a string with the python representation of the instance."""
        return "Flag <%s> (%s)" % (self.name, self.description)

    def __bool__(self):
        """Return a boolean value"""
        return self.value

    def __nonzero__(self):
        return self.__bool__()

    @docstring_property(__doc__)
    def __doc__(self):
        """Return a documentation string, something like:

        {name}: {default}, suppress required {supress}
            {description}

        >>>  flag = Flag(diz=dict(name='a', description='Flag description',
        ...                      default=True))
        >>> print(flag.__doc__)
        a: True
            Flag description

        >>> flag = Flag(diz=dict(name='overwrite'))
        >>> print(flag.__doc__)
        overwrite: None
            None

        """
        return read.DOC["flag"].format(
            name=self.name,
            default=repr(self.default),
            description=self.description,
            supress=("suppress required" if self.suppress_required else ""),
        )
