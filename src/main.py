import sys
import asyncio
import typing as t
from lagom.container import Container
from lagom.definitions import Singleton

from composition_renderer import CompositionExecuter
from composition_providers import CompositionProvider, LayerProvider
from composition_readers import CompositionReader, LayerReader
import generic_types as agt
from input import hardcoded_layers


async def _main(composition: agt.Composition) -> t.NoReturn:
    container = Container()
    container[agt.Composition] = agt.Composition(composition.resolution,
                                                 composition.framerate,
                                                 composition.duration,
                                                 composition.data)

    container[CompositionProvider] = Singleton(CompositionReader)  # type: ignore
    container[LayerProvider] = Singleton(LayerReader)  # type: ignore
    container[CompositionExecuter] = Singleton(CompositionExecuter)

    reader = container[CompositionReader]
    spec = await reader.provide_composition_spec(container[agt.Composition])  # type: ignore
    composition_executer = container[CompositionExecuter]
    await composition_executer.execute(spec)
    print('done')


if __name__ == "__main__":

    if sys.platform.startswith("win") and sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    layers = []

    for layer in hardcoded_layers:

        l_type, l_name, l_args = layer[0], None, None

        if isinstance(layer[1], str):
            l_name = layer[1]
            try:
                l_args = layer[2]
            except:
                ...
        elif isinstance(layer[1], dict):
            l_args = layer[1]
        layers.append(agt.Layer(layer_type=l_type,
                                layer_name=l_name,
                                layer_args=l_args))

    composition = agt.Composition(
        resolution=agt.Resolution('1080'),
        framerate=agt.Framerate(25),
        duration=agt.Duration(5),
        data=layers
    )
    print(composition)
    asyncio.run(_main(composition))
