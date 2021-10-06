import abc
from typing import Type
from typing import TypeVar
from typing import NewType
from typing import Optional
from typing import List
from typing import NamedTuple
from typing import Dict
from typing import Any
from typing import Generic
from typing import Union
from typing import Protocol
from typing import Callable

from functools import partial

from moviepy.editor import ImageClip, ImageSequenceClip, ColorClip, VideoClip, VideoFileClip, TextClip  # type: ignore

T = TypeVar("T")
G_T = Generic[T]
Name = Optional[str]
ARGS = Dict[str, Any]
ClipType = Union[ImageClip, ImageSequenceClip, VideoClip, ColorClip, VideoFileClip, TextClip]
Resolution = NewType("Resolution", str)
Framerate = NewType("Framerate", int)
Duration = NewType("Duration", int)



class Constructable(Protocol):
    def __new__(self,
                  fn: Callable,
                  ar: tuple,
                  kw: dict):
        return lambda fn, ar, kw: partial(fn, ar, kw)


class Layer:
    def __init__(self, source: Constructable) -> None:
        self = source


class Composition(NamedTuple):
    resolution: Resolution
    framerate: Framerate
    duration: Duration
    data: List[Layer]
