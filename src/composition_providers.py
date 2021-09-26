from abc import ABC, abstractmethod
import typing as t
from moviepy.editor import CompositeVideoClip
from composition_validators import CompositionSpec
import generic_types as app_types


class LayerProvider(ABC):
    @abstractmethod
    def build(self,
              layer_type: app_types.T,
              layer_name: app_types.Name,
              layer_args: app_types.ARGS
              ) -> app_types.T:
        pass


class CompositionProvider(ABC):
    @abstractmethod
    def render_composition(self, composition_spec: CompositionSpec) -> CompositeVideoClip:
        pass
