import typing as t
from typing import Any, Type, NamedTuple

T = t.TypeVar("T")
A = t.TypeVar("A")
Name = t.Optional[str]
ARGS = t.Union[A, t.Dict[str, A]]
Resolution = t.NewType("Resolution", str)
Framerate = t.NewType("Framerate", int)
Duration = t.NewType("Duration", int)
LayerData = t.Tuple[T, t.Optional[str], t.Optional[ARGS]]
