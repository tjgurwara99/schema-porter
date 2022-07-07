"""Pydantic converters."""

import inspect
from jinja2 import Environment, PackageLoader, select_autoescape

_env = Environment(
    loader=PackageLoader(package_name="porter.converters"),
    autoescape=select_autoescape(),
)


def pydantic_to_dataclass(cls):
    """Pydantic models to dataclass converter."""
    template = _env.get_template("dataclass_template.tmpl")
    return template.render(
        cls=cls, inspect=inspect, isinstance=isinstance, type=type, str=str
    )


def dataclass_to_pydantic(cls):
    """Convert the serializer from dataclass to a pydantic serialzer."""
    template = _env.get_template("pydantic_template.tmpl")
    return template.render(
        cls=cls, inspect=inspect, isinstance=isinstance, type=type, str=str
    )
