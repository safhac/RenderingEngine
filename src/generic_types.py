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

from moviepy.editor import ImageClip, ImageSequenceClip, ColorClip, VideoClip, VideoFileClip, TextClip  # type: ignore

T = TypeVar("T")
T_T = Type[T]
G_T = Generic[T]
Name = Optional[str]
ARGS = Dict[str, Any]
ClipType = Union[ImageClip, ImageSequenceClip, VideoClip, ColorClip, VideoFileClip, TextClip]
Resolution = NewType("Resolution", str)
Framerate = NewType("Framerate", int)
Duration = NewType("Duration", int)


class Layer(NamedTuple):
    layer_type: ClipType
    layer_name: Name
    layer_args: ARGS



class Composition(NamedTuple):
    resolution: Resolution
    framerate: Framerate
    duration: Duration
    data: List[Layer]
