# matte


[Parameter Types](/documentation/shadergraph/compositing/matte#Parameter-Types)
-------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter descriptions](/documentation/shadergraph/compositing/matte#Parameter-descriptions)
---------------------------------------------------------------------------------------------

`Foreground` 

 The
 `color4` 
 foreground input.
 `F` 
 represents the RGB component of this parameter.
 `f` 
 represents the alpha component of this parameter.
 

`Background` 

 The
 `color4` 
 background input.
 `B` 
 represents the RGB component of this parameter.
 `b` 
 represents the alpha component of this parameter.
 

`Mix` 

 The weight of the blend operation. The higher the value of
 `Mix` 
 , the more apparent the effect of the blend operation. The default value is
 `1` 
 . Values outside of the range
 `0-1` 
 produce an undefined effect outside of the node’s intended function.
 

[Discussion](/documentation/shadergraph/compositing/matte#Discussion)
---------------------------------------------------------------------

 The Matte node determines its output using the alpha channels of the foreground and background inputs. The RGB component of the output is
 `Ff+B(1-f)` 
 and the alpha component of the output is
 `f+b(1-f)` 
 . Below is a simple node graph that uses the In node to blend a wood and rock texture.
 

![](https://docs-assets.developer.apple.com/published/c9896f648bad20c84ad337c69fac5ca0/MatteGraph.png)

 Below are the two original images, the image representation of the alpha of the foreground, and the resulting blended texture applied to a cube.
 

![](https://docs-assets.developer.apple.com/published/aeaf3eaedbb1788dd10bf6b091c35397/MaskMaterial1.png)

 Foreground
 

![](https://docs-assets.developer.apple.com/published/c5085a56de96794b0a52e09d7596a2d4/MaskMaterialAlpha.png)

 Foreground Alpha
 

![](https://docs-assets.developer.apple.com/published/12a56b955ca2c7eaf5c644f2ae3b9464/DisjointOverMaterial2.png)

 Background
 

![](https://docs-assets.developer.apple.com/published/8ae875713c6e485fd5cfa686168f841e/MatteMaterial.png)

 Blended texture
 

 A merge operation that layers premultiplied foreground over background.

[See Also](/documentation/shadergraph/compositing/matte#see-also)
-----------------------------------------------------------------

### [Nodes](/documentation/shadergraph/compositing/matte#nodes)

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
 
