import typing as t

from composition_validators import LayerSpec, CompositionSpec
from composition_providers import LayerProvider, CompositionProvider

import generic_types as agt


class LayerReader(LayerProvider):

    async def provide_layer_spec(self,
                                 layer_type: t.Type[agt.T],
                                 layer_name: t.Optional[agt.Name],
                                 layer_args: t.Optional[agt.ARGS]) -> LayerSpec:
        return LayerSpec(layer_type=layer_type,
                         layer_name=layer_name,
                         layer_args=layer_args)

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


class CompositionReader(CompositionProvider):
    def __init__(self,
                 layer_reader: LayerReader) -> None:
        self.layer_reader = layer_reader

    async def provide_composition_spec(
        self,
        composition: agt.Composition
    ) -> CompositionSpec:
        layers = []

        for layer in composition.data:
            layers.append(await self.layer_reader.provide_layer_spec(layer_type=layer.layer_type,
                                                                     layer_name=layer.layer_name,
                                                                     layer_args=layer.layer_args))

        return CompositionSpec(resolution=composition.resolution,
                               framerate=composition.framerate,
                               duration=composition.duration,
                               data=layers)
