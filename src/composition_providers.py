from abc import ABC, abstractmethod
import typing as t
from composition_validators import CompositionSpec, LayerSpec
import generic_types as agt


class LayerProvider(ABC):

    @abstractmethod
    async def provide_layer_spec(self,
                                 layer_type: t.Type[agt.T],
                                 layer_name: t.Optional[agt.Name],
                                 layer_args: t.Optional[agt.ARGS]
                                 ) -> LayerSpec:
        ...


class CompositionProvider(ABC):
    @abstractmethod
    async def provide_composition_spec(self,
                                       composition: agt.Composition
                                       ) -> CompositionSpec:
        ...
