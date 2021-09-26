import typing as t
from moviepy.editor import CompositeVideoClip
from composition_validators import CompositionSpec
from composition_providers import CompositionProvider
from composition_readers import CompositionReader


class CompositionRenderer:
    def __init__(self, composition_provider: CompositionProvider) -> t.NoReturn:
        self.__compositionRenderer = composition_provider

    async def render(self, composition: CompositionReader) -> CompositeVideoClip:
        layers = []

        for layer in composition.data:
            layers.append(await layer.build())

        with CompositeVideoClip(layers, size=composition.size) as video:
            video.duration = composition.duration
            video.target_resolution = composition.resolution
            video.write_videofile(f'output_movie.mp4')
            map(lambda c: c.close(), layers)


class CompositionExecuter:
    def __init__(
        self,
        composition_reader: CompositionReader,
        composition_renderer: CompositionRenderer
    ) -> t.NoReturn:
        self.__composition_reader = composition_reader
        self.__composition_renderer = composition_renderer

    async def execute(self,
                      composition_parameters: CompositionSpec
                      ) -> t.NoReturn:
        composition_data = await self.__composition_reader.provide_composition_spec(composition_parameters)
        await self.__composition_renderer.render(composition_data)
