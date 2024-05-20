# overlay


[Parameter Types](/documentation/shadergraph/compositing/overlay#Parameter-Types)
---------------------------------------------------------------------------------

* [Overlay (float)](#)
* [Overlay (color3f)](#)
* [Overlay (half)](#)
* [Overlay (color4f)](#)

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

[Parameter descriptions](/documentation/shadergraph/compositing/overlay#Parameter-descriptions)
-----------------------------------------------------------------------------------------------

`Foreground` 

 The foreground input. Represented by
 `F` 
 in the mathmatical equation.
 

`Background` 

 The background input. Represented by
 `B` 
 in the mathmatical equation.
 

`Mix` 

 The weight of the blend operation. The higher the value of
 `Mix` 
 , the more apparent the effect of the blend operation. The default value is
 `1` 
 . Values outside of the range
 `0-1` 
 produce an undefined effect outside of the node’s intended function.
 

[Discussion](/documentation/shadergraph/compositing/overlay#Discussion)
-----------------------------------------------------------------------

 The Overlay node has one of two effects. If
 `F+B` 
 is less than
 `0
 
 .5` 
 , then the node outputs a value of
 `2*F*B` 
 . If
 `F+B` 
 is greater than or equal to
 `0
 
 .5` 
 , then it outputs
 `1-(1-F)(1-B)` 
 , which creates the same visual effect as the
 [`Screen`](/documentation/shadergraph/compositing/screen)
 node. Visually the node makes dark areas of the blended texture even darker and light areas of the blended texture even lighter.
 

 Below is an example of a simple node graph that uses the Overlay node to blend two images together into a single material.
 

![](https://docs-assets.developer.apple.com/published/7ceec91d585b58948afa1611c167fc34/OverlayGraph.png)

 Below are two images and their resulting blended texture applied to a cube.
 

![](https://docs-assets.developer.apple.com/published/e45e991961c71db9bffaaa651cdcaf4a/OverlayMaterial1.png)

 Foreground
 

![](https://docs-assets.developer.apple.com/published/8a7108508e5cad0fbc50f6d6bdc4a006/ScreenMaterial1.png)

 Background
 

![](https://docs-assets.developer.apple.com/published/e2d08d8613e4333f8d28526d6c713847/OverlayMaterial2.png)

 A blend operation that multiplies dark areas and screens light areas.

[See Also](/documentation/shadergraph/compositing/overlay#see-also)
-------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/overlay#nodes)

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
 

