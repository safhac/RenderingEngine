import sys
import asyncio
from composition_renderer import CompositionExecuter, CompositionRenderer
from composition_providers import CompositionProvider
from composition_readers import CompositionReader
import generic_types as app_types
from input import hardcoded_layers as layers


async def _main() -> None:
    composition_reader = CompositionReader()
    composition_spec = await composition_reader.provide_composition_spec(resolution=app_types.Resolution('1080'),
                                                                   framerate=app_types.Framerate(25),
                                                                   duration=app_types.Duration(5),
                                                                   data=layers)

    composition_executer = CompositionExecuter(composition_spec, composition_reader)
    await composition_executer.execute(composition_spec)


if __name__ == "__main__":

    if sys.platform.startswith("win") and sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(_main())
