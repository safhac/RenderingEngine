#Simple rendering engine 
***
[Background (1 min read)](https://botika.notion.site/Simple-Rendering-Engine-d79edc612996441bb183326a1409b283)

###Composition:
```
class Composition(NamedTuple):
    resolution: Resolution
    framerate: Framerate
    duration: Duration
    data: List[Layer]
```
###Layer:
```
class Layer(NamedTuple):
    layer_type: ClipType
    layer_name: Name
    layer_args: ARGS
```
    
- [x] accept a composition 
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tags</del

###[main]
-_input_
`Composition` 

#[rendering]
`CompositionExecuter`
- initialized with
1. `CompositionReader`
2. `CompositionRenderer`
- methods
1. `execute`
in execute the reader returns the validated data, the validated data is sent to the renderer

`CompositionRenderer`
- initialized with 
1. `LayerRenderer`
- methods
1. `render`
the render loops over the layers and builds the concrete _class_ using the layer's metadata.
> this needs to be loosely coupled from whatever library [moviepy or ffmpeg] is returned.  
- returns the `CompositeVideoClip` 

#[reading]
`CompositionReader` 
- initialized with 
1. `LayerReader` 
- methods
1. `provide_composition_spec` validates each layer using `LayerReader` 
- returns a validated `CompositionSpec`

