"""Simple converters."""

import typing


class Converter(typing.Protocol):
    """Converter protocol to make sure statically everything works as expected."""

    def convert_to_dataclass(self, cls):
        """Convert the serializer to dataclass.

        It should return the text version of what the python file containing the dataclass would look like.
        """

    def convert_from_dataclass(self, cls):
        """Convert the serializer from dataclass to the specific serialzer this Converter handles.

        It should return the text version of what the python file containing the serializer would look like.
        """
