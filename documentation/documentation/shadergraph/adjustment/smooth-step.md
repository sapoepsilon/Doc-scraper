# smooth-step


[Parameter Types](/documentation/shadergraph/adjustment/smooth-step#Parameter-Types)
------------------------------------------------------------------------------------

* [Smooth Step (float)](#)
* [Smooth Step (color3f FA)](#)
* [Smooth Step (vector2h FA)](#)
* [Smooth Step (vector2f)](#)
* [Smooth Step (vector2f FA)](#)
* [Smooth Step (vector3f FA)](#)
* [Smooth Step (half)](#)
* [Smooth Step (vector3f)](#)
* [Smooth Step (vector4h)](#)
* [Smooth Step (vector4f FA)](#)
* [Smooth Step (vector3h FA)](#)
* [Smooth Step (vector4f)](#)
* [Smooth Step (vector4h FA)](#)
* [Smooth Step (color3f)](#)
* [Smooth Step (vector2h)](#)
* [Smooth Step (color4f)](#)
* [Smooth Step (color4f FA)](#)
* [Smooth Step (vector3h)](#)

| Input | Type |
| --- | --- |
| `In` | Float |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Vector2f |
| `High` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Half |
| `Low` | Half |
| `High` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Vector3f |
| `High` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Vector4h |
| `High` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Vector4f |
| `High` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Color3 |
| `High` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Vector2h |
| `High` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Color4 |
| `High` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Vector3h |
| `High` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

[Parameter descriptions](/documentation/shadergraph/adjustment/smooth-step#Parameter-descriptions)
--------------------------------------------------------------------------------------------------

`In` 

 The input value to remap.
 

`Low` 

 The low end value of the input range. The default value is
 `0
 
 .0` 
 .
 

`High` 

 The high end value of the input range. The default value is
 `1
 
 .0` 
 .
 

[Discussion](/documentation/shadergraph/adjustment/smooth-step#Discussion)
--------------------------------------------------------------------------

 The Smooth Step node outputs a smooth remapping using hermite-interpolation. Any input with a value lower than the
 `Low` 
 parameter results in an output of
 `0` 
 . Any input with a value higher than the
 `High` 
 parameter results in an output of
 `1` 
 .
 

 Outputs a smooth remapping from low-high to 0-1.

[See Also](/documentation/shadergraph/adjustment/smooth-step#see-also)
----------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/smooth-step#nodes)

[`Remap`](/documentation/shadergraph/adjustment/remap)

 Linearly remaps incoming values from one range to another.
 

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
 

[`Step (Reality
  Kit)`](/documentation/shadergraph/adjustment/step-(realitykit))

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
 

