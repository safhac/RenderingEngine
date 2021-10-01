from pydantic import BaseModel, validator
import typing as t
import inspect
from moviepy.editor import ImageClip, ImageSequenceClip, ColorClip, TextClip, VideoClip, VideoFileClip

import generic_types as agt

moviepytypes = [ImageClip, ImageSequenceClip, ColorClip, TextClip, VideoClip, VideoFileClip]


class LayerSpec(BaseModel):
    layer_type: t.Type[agt.ClipType]
    layer_name: agt.Name = None
    layer_args: agt.ARGS = None

    class Config:
        allow_mutation = False
        arbitrary_types_allowed = True

    @validator('layer_name', pre=True, always=True)
    def set_layer_name(cls, layer_name, values):
        print('set_layer_name')
        print(layer_name)
        return layer_name or None

    @validator('layer_args')
    def set_layer_args(cls, layer_args, values):
        print('set_layer_args')
        print(layer_args)

        if isinstance(layer_args, dict):
            copy_args = layer_args.copy()
            if copy_args.get('duration', None):

                del copy_args['duration']
            layer_type = values['layer_type']
            clip_args = list(inspect.signature(layer_type.__init__).parameters.keys())

            if not all(arg in clip_args for arg in copy_args.keys()):
                print(layer_args)
                print(clip_args)
                raise AttributeError(layer_args, "wrong __init__ parameter")


class CompositionSpec(BaseModel):
    """"""
    resolution: agt.Resolution
    framerate: agt.Framerate
    duration: agt.Duration
    data: t.List[LayerSpec]

    class Config:
        allow_mutation = False
