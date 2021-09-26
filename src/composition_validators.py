from pydantic import BaseModel, validator
import typing as t
import inspect

import generic_types as app_types


class LayerSpec(BaseModel):
    clip_type: app_types.T
    clip_name: app_types.Name
    clip_args: app_types.ARGS

    @validator('clip_args')
    @classmethod
    def clip_args_valid(cls, v, values, **kwargs):
        """validate that clip_args keys are part of the class __init__"""
        if isinstance(v, dict):
            param_names = list(v.keys())
            clip_type = values['clip_type']
            clip_params = list(inspect.signature(clip_type.__init__).parameters.keys())

            if not all(param in clip_params for param in param_names):
                print(param_names)
                print(clip_params)
                raise AttributeError(v, "wrong __init__ parameter")


class CompositionSpec(BaseModel):
    """"""
    resolution: app_types.Resolution
    framerate: app_types.Framerate
    duration: app_types.Duration
    data: t.List[LayerSpec]

    class Config:
        allow_mutation = False
