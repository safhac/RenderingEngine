# Simple rendering engine

***
[Background (1 min read)](https://botika.notion.site/Simple-Rendering-Engine-d79edc612996441bb183326a1409b283)
***

#### Composition:

```
class Composition(NamedTuple):
    resolution: Resolution
    framerate: Framerate
    duration: Duration
    data: List[Layer]
```

#### Layer:

```
class Layer(NamedTuple):
    layer_type: ClipType
    layer_name: Name
    layer_args: ARGS
```

***

#### Executer:

```
class CompositionExecuter:
    
    def __init__(CompositionReader, CompositionRenderer)
    
    def execute(Composition):
        validated_data = reader.validate(composition)
        await renderer.render(validated_data)
    
```

#### Renderer:

```
class CompositionRenderer:
    
    def __init__(LayerRenderer)
        
    def render(CompositionSpec):
        instatiate each layer using _module_  
        ...    
        process the composition rendering 
``` 

#### Reader:

```
class CompositionReader(CompositionProvider):
    
    def __init__(LayerReader)
        
    def provide_composition_spec(Composition)-> CompositionSpec:
        validate each layer using LayerReader 
        ...    
        return validated Composition 
``` 

#### Validation:

```
class LayerSpec(BaseModel):
    1. provide generic mechanism to validate variadic 3rd party _module_ classes
    2. validate layer type belongs to _module_
    3. validate layer arguments are legal to the type
    
``` 
