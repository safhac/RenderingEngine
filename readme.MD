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
> loosely coupled to whatever library [moviepy or ffmpeg] is returned.  


#[reading]
`CompositionReader` 
- initialized with 
1. `LayerReader` 
- methods
1. `provide_composition_spec` validates the layers using `LayerReader` and returns a validated `CompositionSpec`

