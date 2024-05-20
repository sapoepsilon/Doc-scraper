# luminance


[Parameter Types](/documentation/shadergraph/adjustment/luminance#Parameter-Types)
----------------------------------------------------------------------------------

* [Luminance (color3f)](#)
* [Luminance (color4f)](#)

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter descriptions](/documentation/shadergraph/adjustment/luminance#Parameter-descriptions)
------------------------------------------------------------------------------------------------

`In` 

 The input to convert to grayscale.
 

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
 

[Discussion](/documentation/shadergraph/adjustment/luminance#Discussion)
------------------------------------------------------------------------

 The Luminance node takes in a color input and outputs that input as a grayscale image. The node computes the grayscale of an image by taking the dot product of the luma coefficients and the color vector. Below is an example of a simple node graph that uses the luminance node to convert an image to grayscale.
 

![](https://docs-assets.developer.apple.com/published/42414e1db5a8fb66784619ba91aeb247/LuminanceGraph.png)

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/04c91b365ba7d80a94adf26a6efe8284/LuminanceMaterial.png)

 Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.

[See Also](/documentation/shadergraph/adjustment/luminance#see-also)
--------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/luminance#nodes)

[`Remap`](/documentation/shadergraph/adjustment/remap)

 Linearly remaps incoming values from one range to another.
 

[`Smooth Step`](/documentation/shadergraph/adjustment/smooth-step)

 Outputs a smooth remapping from low-high to 0-1.
 

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
 

[`Saturate`](/documentation/shadergraph/adjustment/saturate)

 Adjusts the saturation of a color.
 

[`Step (Reality Kit)`](/documentation/shadergraph/adjustment/step-(realitykit))

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
 

