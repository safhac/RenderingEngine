#[main]
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

