# dodge


[Parameter Types](/documentation/shadergraph/compositing/dodge#Parameter-Types)
-------------------------------------------------------------------------------

* [Dodge (float)](#)
* [ND\_dodge\_half](#)
* [Dodge (color3f)](#)
* [Dodge (color4f)](#)

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
| `Foreground` | Half |
| `Background` | Half |
| `Mix` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

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

[Parameter Description](/documentation/shadergraph/compositing/dodge#Parameter-Description)
-------------------------------------------------------------------------------------------

`Foreground` 

 The foreground input. Represented by
 `F` 
 in the mathmatical equation.
 

`Background` 

 The background input. Represented by
 `B` 
 in the mathmatical equation.
 

`Mix` 

 The weight of the blend operation. The higher the
 `Mix` 
 , the greater the intensity of the blend operation, and the more the effect is visually apparent. The default value is
 `1` 
 . Values outside of the range
 `0-1` 
 produce an undefined effect outside of the node’s intended function.
 

[Discussion](/documentation/shadergraph/compositing/dodge#Discussion)
---------------------------------------------------------------------

 The Dodge node lightens each area in the background based on the lightness of the corresponding area in the foreground, represented by the equation
 `B / (1 - F)` 
 . Below is an example of a simple node graph that uses the the dodge node to lighten a brick texture.
 

![](https://docs-assets.developer.apple.com/published/4aa9b8b032d8716a4316e8c991c36f25/DodgeGraph.png)

 Use a
 [`Noise 2D`](/documentation/shadergraph/2d-procedural/noise-2d)
 node to generate Perlin noise, and use the output of that texture as the foreground in the dodge node. This process causes the background brick texture to lighten according to the procedural pattern. Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/3f99d156c5fbb66084cdaecc9ea0b4ec/DodgeMaterial.png)

 A blend operation that lightens the background layer depending on the foreground.

[See Also](/documentation/shadergraph/compositing/dodge#see-also)
-----------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/dodge#nodes)

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
 

