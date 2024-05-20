# outside


[Parameter Types](/documentation/shadergraph/compositing/outside#Parameter-Types)
---------------------------------------------------------------------------------

* [Outside (float)](#)
* [Outside (half)](#)
* [Outside (color3f)](#)
* [Outside (color4f)](#)

| Input | Type |
| --- | --- |
| `In` | Float |
| `Mask` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Half |
| `Mask` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Mask` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Mask` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter descriptions](/documentation/shadergraph/compositing/outside#Parameter-descriptions)
-----------------------------------------------------------------------------------------------

`In` 

 The input value to which the mask applies.
 

`Mask` 

 The value by which the input is multiplied.
 

[Discussion](/documentation/shadergraph/compositing/outside#Discussion)
-----------------------------------------------------------------------

 Below is an example of a simple node graph that uses the Outside node to apply a mask to a brick texture.
 

![](https://docs-assets.developer.apple.com/published/fa72f1155b0049c8effbed2bbc869017/OutsideGraph.png)

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/22d385b227fa57a9a3f445794e022e8e/InsideMaterial1.png)

 Mask
 

![](https://docs-assets.developer.apple.com/published/b8a12d9ac1244a778a30d88ebfe67b03/InsideMaterial2.png)

 Input
 

![](https://docs-assets.developer.apple.com/published/38b4a6a44aa78ba48dc64c3a582f6f37/OutsideMaterial.png)

 Multiplies (1 - mask) to all channels of the input.

[See Also](/documentation/shadergraph/compositing/outside#see-also)
-------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/outside#nodes)

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
 

[`Mix`](/documentation/shadergraph/compositing/mix)

 Mixes foreground and background inputs, weighting based on mix value.
 

