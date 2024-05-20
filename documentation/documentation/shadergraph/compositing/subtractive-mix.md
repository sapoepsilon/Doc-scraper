# subtractive-mix


[Parameter Types](/documentation/shadergraph/compositing/subtractive-mix#Parameter-Types)
-----------------------------------------------------------------------------------------

* [Subtractive Mix (float)](#)
* [Subtractive Mix (color3f)](#)
* [Subtractive Mix (half)](#)
* [Subtractive Mix (color4f)](#)

| Input | Type |
| --- | --- |
| `Foreground` | Float |
| `Background` | Float |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Foreground` | Color3 |
| `Background` | Color3 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Foreground` | Half |
| `Background` | Half |
| `Mix` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter descriptions](/documentation/shadergraph/compositing/subtractive-mix#Parameter-descriptions)
-------------------------------------------------------------------------------------------------------

`Foreground` 

 The foreground input. Represented by
 `F` 
 in the mathmatical equation.
 

`Background` 

 The background input. Represented by
 `B` 
 in the mathmatical equation.
 

`Mix` 

 The weight of the blend effect. The higher the
 `Mix` 
 , the greater the intensity of the blend operation, and the more the effect is visually apparent. The default value is
 `1` 
 . Values outside of the range
 `0-1` 
 produce an undefined effect outside of the node’s intended function.
 

[Discussion](/documentation/shadergraph/compositing/subtractive-mix#Discussion)
-------------------------------------------------------------------------------

 The Subtractive Mix node subtracts two inputs and uses the
 `Mix` 
 input to determine the weight of the foreground in the blend, represented by the equation
 `B - F` 
 . Higher values closer to
 `1` 
 output a more intense subtractive mix, while lower values closer to
 `0` 
 dim the effect. Below is an example of a simple node graph that uses the subtractive mix node to blend two images together into a single material.
 

![](https://docs-assets.developer.apple.com/published/0b2cb1c29296c2d895fde15bce065e41/SubtractiveMixGraph.png)

 Below are two images and the resulting blended texture applied to a cube.
 

![](https://docs-assets.developer.apple.com/published/d9c4946e10d4cea53d216d891a402e72/MixMaterial1.png)

 Foreground
 

![](https://docs-assets.developer.apple.com/published/894072a80859e854d9facc19ef5e6577/BrickTexture.png)

 Background
 

![](https://docs-assets.developer.apple.com/published/fca33a7dff83ead7e54cef9ff64f0775/SubtractiveMixMaterial.png)

 Subtracts foreground from background values.

[See Also](/documentation/shadergraph/compositing/subtractive-mix#see-also)
---------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/subtractive-mix#nodes)

[`Premultiply`](/documentation/shadergraph/compositing/premultiply)

 Multiplies the RGB channels of the input by the alpha channel.
 

[`Unpremultiply`](/documentation/shadergraph/compositing/unpremultiply)

 Divides the RGB channels of the input by the alpha channel.
 

[`Additive Mix`](/documentation/shadergraph/compositing/additive-mix)

 Adds foreground and background values.
 

[`Difference`](/documentation/shadergraph/compositing/difference)

 Outputs the distance between foreground and background values.
 

[`Burn`](/documentation/shadergraph/compositing/burn)

 A blend operation that darkens the foreground layer using the background.
 

[`Dodge`](/documentation/shadergraph/compositing/dodge)

 A blend operation that lightens the background layer depending on the foreground.
 

[`Screen`](/documentation/shadergraph/compositing/screen)

 A blend operation that lightens areas that are darker than white.
 

[`Overlay`](/documentation/shadergraph/compositing/overlay)

 A blend operation that multiplies dark areas and screens light areas.
 

[`Disjoint Over`](/documentation/shadergraph/compositing/disjoint-over)

 A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.
 

[`In`](/documentation/shadergraph/compositing/in)

 Outputs areas of foreground that overlap with the alpha of background.
 

[`Mask`](/documentation/shadergraph/compositing/mask)

 Outputs areas of background that overlap with the alpha of foreground.
 

[`Matte`](/documentation/shadergraph/compositing/matte)

 A merge operation that layers premultiplied foreground over background.
 

[`Out`](/documentation/shadergraph/compositing/out)

 Outputs areas of foreground that do not overlap with background.
 

[`Over`](/documentation/shadergraph/compositing/over)

 A merge operation that layers foreground over background, using the alpha of the foreground.
 

[`Inside`](/documentation/shadergraph/compositing/inside)

 Multiplies a mask to all channels of the input.
 

[`Outside`](/documentation/shadergraph/compositing/outside)

 Multiplies (1 - mask) to all channels of the input.
 

[`Mix`](/documentation/shadergraph/compositing/mix)

 Mixes foreground and background inputs, weighting based on mix value.
 

