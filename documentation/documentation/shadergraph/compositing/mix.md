# mix


[Parameter Types](/documentation/shadergraph/compositing/mix#Parameter-Types)
-----------------------------------------------------------------------------

* [Mix (float)](#)
* [Mix (color3f)](#)
* [Mix (color4f)](#)
* [Mix (vector3h)](#)
* [Mix (half)](#)
* [Mix (vector4f)](#)
* [Mix (vector4h)](#)
* [Mix (vector2h)](#)
* [Mix (vector2f)](#)
* [Mix (vector3f)](#)

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
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Foreground` | Vector3h |
| `Background` | Vector3h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

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
| `Foreground` | Vector4f |
| `Background` | Vector4f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `Foreground` | Vector4h |
| `Background` | Vector4h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `Foreground` | Vector2h |
| `Background` | Vector2h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `Foreground` | Vector2f |
| `Background` | Vector2f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Foreground` | Vector3f |
| `Background` | Vector3f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/compositing/mix#Parameter-descriptions)
-------------------------------------------------------------------------------------------

`Foreground` 

 The foreground input.
 

`Background` 

 The background input.
 

`Mix` 

 The weight that determines what the output value is closer to. The default value is
 `0` 
 . Values outside of the range
 `0-1` 
 produce an undefined effect outside of the node’s intended function.
 

[Discussion](/documentation/shadergraph/compositing/mix#Discussion)
-------------------------------------------------------------------

 The Mix node blends two input values together, represented by the equation
 `F * m + B(1 - m)` 
 . If the
 `Mix` 
 value is
 `1` 
 , the output is identical to the
 `Foreground` 
 value. If the value is
 `0` 
 , the output is identical to the
 `Background` 
 value. The closer the
 `Mix` 
 value is to
 `0` 
 or
 `1` 
 , the closer the output will be to the corresponding input. Use the Mix node to blend between two different textures and create transtions or effects, interpolate between two colors, or mix shader parameters. Below is an example of a simple node graph that uses the Mix node to blend two images together into a single material.
 

![](https://docs-assets.developer.apple.com/published/b3384b6745c8bc85f86c162a23029dde/MixGraph.png)

 Below are the original two images and the resulting mixed texture applied to a cube with
 `Mix` 
 values of
 `0
 
 .1` 
 ,
 `0
 
 .5` 
 , and
 `0
 
 .9` 
 .
 

![](https://docs-assets.developer.apple.com/published/d9c4946e10d4cea53d216d891a402e72/MixMaterial1.png)

 Foreground
 

![](https://docs-assets.developer.apple.com/published/b441e81d3c5f432f986de82ef398e0bd/MixMaterial2.png)

 Background
 

![](https://docs-assets.developer.apple.com/published/85abb3ae1748aea61e4792eba13c0b53/MixMaterial3.png)

 Mix value of 0.1
 

![](https://docs-assets.developer.apple.com/published/9e0e012f49a5a7b86da825233bb28a94/MixMaterial4.png)

 Mix value of 0.5
 

![](https://docs-assets.developer.apple.com/published/08a96c1a93d87a37c1c1b62083807b56/MixMaterial5.png)

 Mix value of 0.9
 

 Mixes foreground and background inputs, weighting based on mix value.

[See Also](/documentation/shadergraph/compositing/mix#see-also)
---------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/mix#nodes)

[`Premultiply`](/documentation/shadergraph/compositing/premultiply)

 Multiplies the RGB channels of the input by the alpha channel.
 

[`Unpremultiply`](/documentation/shadergraph/compositing/unpremultiply)

 Divides the RGB channels of the input by the alpha channel.
 

[`Additive Mix`](/documentation/shadergraph/compositing/additive-mix)

 Adds foreground and background values.
 

[`Subtractive Mix`](/documentation/shadergraph/compositing/subtractive-mix)

 Subtracts foreground from background values.
 

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
 

