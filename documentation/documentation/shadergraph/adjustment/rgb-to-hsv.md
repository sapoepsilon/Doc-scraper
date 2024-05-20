# rgb-to-hsv


[Parameter Types](/documentation/shadergraph/adjustment/rgb-to-hsv#Parameter-Types)
-----------------------------------------------------------------------------------

* [RGB to HSV (color3f)](#)
* [RGB to HSV (color4f)](#)

| Input | Type |
| --- | --- |
| `In` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

 Converts a color from RGB to HSV space.

[See Also](/documentation/shadergraph/adjustment/rgb-to-hsv#see-also)
---------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/rgb-to-hsv#nodes)

[`Remap`](/documentation/shadergraph/adjustment/remap)

 Linearly remaps incoming values from one range to another.
 

[`Smooth Step`](/documentation/shadergraph/adjustment/smooth-step)

 Outputs a smooth remapping from low-high to 0-1.
 

[`Luminance`](/documentation/shadergraph/adjustment/luminance)

 Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.
 

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
 

[`Step (Reality
  Kit)`](/documentation/shadergraph/adjustment/step-(realitykit))

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
 

