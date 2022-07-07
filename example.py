"""Some example usage."""

import dataclasses
import pydantic
import typing
from porter.converters.pydantic_converter import pydantic_to_dataclass, dataclass_to_pydantic


class Something(pydantic.BaseModel):
    """Something."""

    data: int
    list_of_data: typing.List[int]


@dataclasses.dataclass
class SomethingDataclass:
    "Something Dataclass."
    data: int
    list_of_data: typing.List[int]


if __name__ == "__main__":
    rendered_template = dataclass_to_pydantic(Something)
    with open(f"{Something.__name__.lower()}_generated_pydantic.py", "w") as f:
        f.write(rendered_template)
