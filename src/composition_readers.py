import typing as t
from composition_validators import LayerSpec, CompositionSpec
from composition_providers import LayerProvider, CompositionProvider

import generic_types as app_types


class LayerReader(LayerProvider):
    async def provide_layer_spec(
        layer_data: app_types.LayerData
    ) -> LayerSpec:
        return LayerSpec(clip_type=layer_data[0],
                         clip_name=layer_data[1],
                         clip_args=layer_data[2])


class CompositionReader(CompositionProvider):
    async def provide_composition_spec(
        resolution: app_types.Resolution,
        framerate: app_types.Framerate,
        duration: app_types.Duration,
        data: t.List[app_types.LayerData]
    ) -> CompositionSpec:

        layers = []
        reader = LayerReader()
        for layer in data:
            layers.append(await reader.provide_layer_spec(layer))

        return CompositionSpec(resolution=resolution,
                               framerate=framerate,
                               duration=duration,
                               data=layers)
