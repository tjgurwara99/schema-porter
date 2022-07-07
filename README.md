# Schema Porter

A simple code generation tool to port serializers.

For example, suppose you have microservices teams A and B working on something related
and team B is calling team A's microservice to get an object[^1]. Now, they can do that
and but team B heavily relies on `pydantic` BaseModels (for example) but team A uses
`dataclasses` for modelling their object. Now, it isn't difficult to copy and paste to
get it to work in `pydantic` and vice versa but can we not automate this? This project
is an attempt to solve this particular issue.

## Known Issues

1. `PydanticConverter` needs to be improved to resolve import dependencies. 

NOTE: This project is highly experimental, POC. Please use at your own risk.

[^1] Thoughts: is it really a microservice in that case?
