# step-realitykit


[Parameter Types](/documentation/shadergraph/adjustment/step-(realitykit)#Parameter-Types)
------------------------------------------------------------------------------------------

* [Step (float)](#)
* [Step (color3f)](#)
* [Step (color4f)](#)
* [Step (vector3f)](#)
* [Step (vector4f)](#)
* [Step (vector2f)](#)

| Input | Type |
| --- | --- |
| `In` | Float |
| `Edge` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Edge` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Edge` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Edge` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Edge` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Edge` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

[Parameter descriptions](/documentation/shadergraph/adjustment/step-(realitykit)#Parameter-descriptions)
--------------------------------------------------------------------------------------------------------

`In` 

 The input value.
 

`Edge` 

 The deciding value to which to compare the input.
 

[Discussion](/documentation/shadergraph/adjustment/step-(realitykit)#Discussion)
--------------------------------------------------------------------------------

 The Step node takes the
 `In` 
 value and compares it to the
 `Edge` 
 parameter. If the value is less than
 `Edge` 
 , the node returns
 `0` 
 . Otherwise, it returns
 `1` 
 .
 

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.

[See Also](/documentation/shadergraph/adjustment/step-(realitykit)#see-also)
----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/step-(realitykit)#nodes)

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
 

[`Saturate`](/documentation/shadergraph/adjustment/saturate)

 Adjusts the saturation of a color.
 

