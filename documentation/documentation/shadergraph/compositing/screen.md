# screen


[Parameter Types](/documentation/shadergraph/compositing/screen#Parameter-Types)
--------------------------------------------------------------------------------

* [Screen (float)](#)
* [Screen (color3f)](#)
* [ND\_screen\_half](#)
* [Screen (color4f)](#)

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

[Parameter descriptions](/documentation/shadergraph/compositing/screen#Parameter-descriptions)
----------------------------------------------------------------------------------------------

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
 

[Discussion](/documentation/shadergraph/compositing/screen#Discussion)
----------------------------------------------------------------------

 The Screen node inverts the color values of both the foreground and background and multiplies those values together. Then the node inverts the colors again. This is represented by the equation
 `1 - (1 - F)(1 - B)` 
 . The resulting visual effect is always equally bright or brighter than the original textures. Below is an example of a simple node graph that uses the Screen node to blend two images together into a single material.
 

![](https://docs-assets.developer.apple.com/published/28a0a55b18ecac5972bd5ed2e21eebeb/ScreenGraph.png)

 Below are two images and their resulting blended texture applied to a cube.
 

![](https://docs-assets.developer.apple.com/published/7aee9efa7c8a8a4e7b0e64887d4b54f2/ScreenMaterial2.png)

 Foreground
 

![](https://docs-assets.developer.apple.com/published/8a7108508e5cad0fbc50f6d6bdc4a006/ScreenMaterial1.png)

 Background
 

![](https://docs-assets.developer.apple.com/published/5a84eb39e40779bc1d9fb68d07252bf4/ScreenMaterial3.png)

 A blend operation that lightens areas that are darker than white.

[See Also](/documentation/shadergraph/compositing/screen#see-also)
------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/screen#nodes)

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
 

