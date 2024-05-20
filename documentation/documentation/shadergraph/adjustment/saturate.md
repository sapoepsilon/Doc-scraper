# saturate


[Parameter Types](/documentation/shadergraph/adjustment/saturate#Parameter-Types)
---------------------------------------------------------------------------------

* [Saturate (color3f)](#)
* [Saturate (color4f)](#)

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Amount` | Float |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Amount` | Float |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter descriptions](/documentation/shadergraph/adjustment/saturate#Parameter-descriptions)
-----------------------------------------------------------------------------------------------

`In` 

 The input color to adjust the saturation of.
 

`Amount` 

 The multiplier to apply to the saturation. The default value is
 `1
 
 .0` 
 .
 

`Luma Coefficients` 

 The luma coefficients of the color space. The possible values for this node are the luma coeffiecients for the color spaces
 `acescg` 
 ,
 `rec202/rec2100` 
 , or
 `rec709` 
 . The default value is the luma coeffiecients for
 `acescg` 
 , which are
 `(0
 
 .2722287, 0
 
 .6740818, 0
 
 .0536895)` 
 .
 

[Discussion](/documentation/shadergraph/adjustment/saturate#Discussion)
-----------------------------------------------------------------------

 The Saturate node performs a linear interpolation between the incoming color value and the luminance of the incoming color value. Setting the value of the
 `Amount` 
 parameter to
 `0` 
 adjusts the output to a grayscale of the input equal to the value that the
 [`Luminance`](/documentation/shadergraph/adjustment/luminance)
 would output.
 

 Note
 

 The effect of this node isn’t equivalent to adjusting saturation with the
 [`HSV Adjust`](/documentation/shadergraph/adjustment/hsv-adjust)
 node. The Saturate node takes into account a colorspace when processing its modifications.
 

 Below is an example of a simple node graph that uses the Saturate node to modify the saturation of an image.
 

![](https://docs-assets.developer.apple.com/published/53fe35cf80e429ddc0ea359e9d067a7c/SaturateGraph.png)

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/894072a80859e854d9facc19ef5e6577/BrickTexture.png)

 Original Texture
 

![](https://docs-assets.developer.apple.com/published/acc8de94cc6c546d57faab8ef7f3eb37/SaturateMaterial1.png)

 Amount: 0.5
 

![](https://docs-assets.developer.apple.com/published/e8d7843e8fc503a84c402100bca4e4ad/SaturateMaterial2.png)

 Amount: 2
 

 Adjusts the saturation of a color.

[See Also](/documentation/shadergraph/adjustment/saturate#see-also)
-------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/saturate#nodes)

[`Remap`](/documentation/shadergraph/adjustment/remap)

 Linearly remaps incoming values from one range to another.
 

[`Smooth Step`](/documentation/shadergraph/adjustment/smooth-step)

 Outputs a smooth remapping from low-high to 0-1.
 

[`Luminance`](/documentation/shadergraph/adjustment/luminance)

 Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.
 

[`RGB to HSV`](/documentation/shadergraph/adjustment/rgb-to-hsv)

 Converts a color from RGB to HSV space.
 

[`HSV to RGB`](/documentation/shadergraph/adjustment/hsv-to-rgb)

 Converts a color from HSV to RGB space.
 

[`Contrast`](/documentation/shadergraph/adjustment/contrast)

 Increases or decreases contrast of values using a linear slope multiplier.
 

[`Range`](/documentation/shadergraph/adjustment/range)

 Remaps incoming values from one range to another.
 

[`HSV Adjust`](/documentation/shadergraph/adjustment/hsv-adjust)

 Adjusts the hue, saturation and value of an RGB color by a vector .
 

[`Step (Reality
  Kit)`](/documentation/shadergraph/adjustment/step-(realitykit))

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
 

