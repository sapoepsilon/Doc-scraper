# remap


[Parameter Types](/documentation/shadergraph/adjustment/remap#Parameter-Types)
------------------------------------------------------------------------------

* [Remap (float)](#)
* [Remap (vector2f)](#)
* [Remap (vector2h FA)](#)
* [Remap (vector2h)](#)
* [Remap (vector4h)](#)
* [Remap (vector4h FA)](#)
* [Remap (vector3h)](#)
* [Remap (vector3h FA)](#)
* [Remap (vector3f)](#)
* [Remap (color4f)](#)
* [Remap (vector3f FA)](#)
* [Remap (color3f FA)](#)
* [Remap (vector2f FA)](#)
* [Remap (color4f FA)](#)
* [Remap (color3f)](#)
* [Remap (half)](#)
* [Remap (vector4f FA)](#)
* [Remap (vector4f)](#)

| Input | Type |
| --- | --- |
| `In` | Float |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `In Low` | Vector2f |
| `In High` | Vector2f |
| `Out Low` | Vector2f |
| `Out High` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `In Low` | Vector2h |
| `In High` | Vector2h |
| `Out Low` | Vector2h |
| `Out High` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `In Low` | Vector4h |
| `In High` | Vector4h |
| `Out Low` | Vector4h |
| `Out High` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `In Low` | Vector3h |
| `In High` | Vector3h |
| `Out Low` | Vector3h |
| `Out High` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `In Low` | Vector3f |
| `In High` | Vector3f |
| `Out Low` | Vector3f |
| `Out High` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `In Low` | Color4 |
| `In High` | Color4 |
| `Out Low` | Color4 |
| `Out High` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `In Low` | Color3 |
| `In High` | Color3 |
| `Out Low` | Color3 |
| `Out High` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Half |
| `In Low` | Half |
| `In High` | Half |
| `Out Low` | Half |
| `Out High` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `In Low` | Float |
| `In High` | Float |
| `Out Low` | Float |
| `Out High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `In Low` | Vector4f |
| `In High` | Vector4f |
| `Out Low` | Vector4f |
| `Out High` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

[Parameter descriptions](/documentation/shadergraph/adjustment/remap#Parameter-descriptions)
--------------------------------------------------------------------------------------------

`In` 

 The input value to be remapped.
 

`In Low` 

 The low end value of the input range. The default value is
 `0
 
 .0` 
 .
 

`In High` 

 The high end value of the input range. The default value is
 `1
 
 .0` 
 .
 

`Out Low` 

 The low end value of the output range. The default value is
 `0
 
 .0` 
 .
 

`Out High` 

 The high end value of the output range. The default value is
 `1
 
 .0` 
 .
 

 Linearly remaps incoming values from one range to another.

[See Also](/documentation/shadergraph/adjustment/remap#see-also)
----------------------------------------------------------------

### [Nodes](/documentation/shadergraph/adjustment/remap#nodes)

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
 

[`Step (Reality
  Kit)`](/documentation/shadergraph/adjustment/step-(realitykit))

 Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
 

