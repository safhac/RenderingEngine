import typing as t
from moviepy.editor import VideoClip, CompositeVideoClip, ColorClip  # type: ignore
from composition_validators import CompositionSpec
from composition_providers import CompositionProvider
from composition_readers import CompositionReader
import generic_types as agt


class LayerRenderer:
    async def build(self,
                    layer_type: t.Callable[..., agt.T],
                    layer_name: t.Optional[agt.Name],
                    layer_args: t.Optional[agt.ARGS]) -> agt.T:

        print(f'layer renderer type {layer_type} name {layer_name} args {layer_args}')

        try:
            if layer_args:

                return layer_type(layer_name, **layer_args)

            else:

                return layer_type(layer_name)

        except Exception as e:
            print(f'{e.args[0]}')
            return layer_type()


class CompositionRenderer:
    def __init__(self, layer_renderer: LayerRenderer) -> None:
        self.layer_renderer = layer_renderer

    async def render(self, composition: CompositionSpec) -> CompositeVideoClip:
        layers = []

        for layer in composition.data:
            with await self.layer_renderer.build(layer_type=layer.layer_type,
                                                 layer_name=layer.layer_name,
                                                 layer_args=layer.layer_args) as clip:
                if layer.layer_args:
                    clip.duration = layer.layer_args.get('duration', composition.duration)
                else:
                    clip.duration = composition.duration

                layers.append(clip)

        with CompositeVideoClip(layers) as video:
            video.duration = composition.duration
            try:
                video.write_videofile(f'output_movie.mp4', audio=None)
            except Exception as e:
                print(f'{e.args[0]}')
            map(lambda c: c.close(), layers)


class CompositionExecuter:
    def __init__(
        self,
        composition_reader: CompositionReader,
        composition_renderer: CompositionRenderer
    ) -> None:
        self.__composition_reader = composition_reader
        self.__composition_renderer = composition_renderer

    async def execute(self,
                      composition_parameters: agt.Composition
                      ) -> t.NoReturn:
        composition_data = await self.__composition_reader.provide_composition_spec(composition_parameters)
        await self.__composition_renderer.render(composition_data)
