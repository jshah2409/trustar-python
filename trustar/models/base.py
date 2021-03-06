# python 2 backwards compatibility
from __future__ import print_function
from builtins import object
from future import standard_library
from six import string_types

# external imports
import json


class ModelBase(object):
    """
    This is the base class for all models.
    """

    def to_dict(self, remove_nones=False):
        """
        Creates a dictionary representation of the object.

        :param remove_nones: Whether ``None`` values should be filtered out of the dictionary.  Defaults to ``False``.
        :return: The dictionary representation.
        """

        if remove_nones:
            return {k: v for k, v in self.to_dict().items() if v is not None}
        else:
            raise NotImplementedError()

    @classmethod
    def from_dict(cls, d):
        """
        Creates an instance of the class from a dictionary representation.
        :return: The instance.
        """
        raise NotImplementedError()

    def __str__(self):
        """
        :return: A json representation of the object.
        """

        return json.dumps(self.to_dict(remove_nones=True), indent=2)

    def __repr__(self):
        """
        :return: The string representation of the object.
        """

        return str(self)
