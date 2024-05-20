# clamp


[Parameter Types](/documentation/shadergraph/math/clamp#Parameter-Types)
------------------------------------------------------------------------

* [Clamp (float)](#)
* [Clamp (color4f)](#)
* [Clamp (vector4f FA)](#)
* [Clamp (vector3h)](#)
* [Clamp (vector2h FA)](#)
* [Clamp (vector4h FA)](#)
* [Clamp (vector3h FA)](#)
* [Clamp (vector4h)](#)
* [Clamp (color4f FA)](#)
* [Clamp (vector4f)](#)
* [Clamp (vector3f)](#)
* [Clamp (half)](#)
* [Clamp (vector3f FA)](#)
* [Clamp (color3f FA)](#)
* [Clamp (vector2f FA)](#)
* [Clamp (vector2h)](#)
* [Clamp (vector2f)](#)
* [Clamp (color3f)](#)

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
| `In` | Color4 |
| `Low` | Color4 |
| `High` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

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
| `Low` | Vector3h |
| `High` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

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
| `In` | Vector4h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

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
| `In` | Vector4h |
| `Low` | Vector4h |
| `High` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

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
| `In` | Vector4f |
| `Low` | Vector4f |
| `High` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

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
| `In` | Half |
| `Low` | Half |
| `High` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

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
| `In` | Color3 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

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
| `In` | Vector2h |
| `Low` | Vector2h |
| `High` | Vector2h |

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
| `In` | Color3 |
| `Low` | Color3 |
| `High` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

[Parameter descriptions](/documentation/shadergraph/math/clamp#Parameter-descriptions)
--------------------------------------------------------------------------------------

`In` 

 The input to be clamped.
 

`Low` 

 The low end of the clamp range.
 

`High` 

 The high end of the clamp range.
 

[Discussion](/documentation/shadergraph/math/clamp#Discussion)
--------------------------------------------------------------

 The Clamp node restricts the range of values of an input; the range of values is defined by the
 `Low` 
 and
 `High` 
 parameters passed into the node. The output of the Clamp node is the same as the
 `In` 
 value if it falls within the defined range. Otherwise, the output is clamped to the nearest limit, which is either the
 `Low` 
 or
 `High` 
 value. Use the Clamp node to create more predictable and controlled shader behavior for materials.
 

 Clamps the input per-channel to a specified range.

[See Also](/documentation/shadergraph/math/clamp#see-also)
----------------------------------------------------------

### [Nodes](/documentation/shadergraph/math/clamp#nodes)

[`Add`](/documentation/shadergraph/math/add)

 Adds two values.
 

[`Subtract`](/documentation/shadergraph/math/subtract)

 Subtracts two values.
 

[`Multiply`](/documentation/shadergraph/math/multiply)

 Multiplies two values.
 

[`Divide`](/documentation/shadergraph/math/divide)

 Divides two values.
 

[`Modulo`](/documentation/shadergraph/math/modulo)

 Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
 

[`Abs`](/documentation/shadergraph/math/abs)

 Outputs the per-channel absolute value of the input.
 

[`Floor`](/documentation/shadergraph/math/floor)

 Outputs the nearest integer value, per-channel, less than or equal to the incoming values.
 

[`Ceiling`](/documentation/shadergraph/math/ceiling)

 Outputs the nearest integer value, per-channel, greater than or equal to the incoming values.
 

[`Power`](/documentation/shadergraph/math/power)

 Raises the incoming value to an exponent.
 

[`Sin`](/documentation/shadergraph/math/sin)

 The sine of the incoming value in radians.
 

[`Cos`](/documentation/shadergraph/math/cos)

 The cosine of the incoming value in radians.
 

[`Tan`](/documentation/shadergraph/math/tan)

 The tangent of the incoming value in radians.
 

[`Asin`](/documentation/shadergraph/math/asin)

 The arcsine of the incoming value in radians.
 

[`Acos`](/documentation/shadergraph/math/acos)

 The arccosine of the incoming value in radians.
 

[`Atan2`](/documentation/shadergraph/math/atan2)

 The arctangent of the expression (iny/inx) in radians.
 

[`Square Root`](/documentation/shadergraph/math/square-root)

 The square root of the incoming value.
 

[`Natural Log`](/documentation/shadergraph/math/natural-log)

 The natural log of the input.
 

[`Exp`](/documentation/shadergraph/math/exp)

 Outputs ‘e’ to the power of the input.
 

[`Sign`](/documentation/shadergraph/math/sign)

 The per-channel sign of the input value: -1 for negative, +1 for positive, 0 for zero.
 

[`Min`](/documentation/shadergraph/math/min)

 Outputs the minimum of two incoming values.
 

[`Max`](/documentation/shadergraph/math/max)

 Outputs the maximum of two incoming values.
 

[`Normalize`](/documentation/shadergraph/math/normalize)

 Outputs a normalized vector.
 

[`Magnitude`](/documentation/shadergraph/math/magnitude)

 Outputs the float magnitude of a vector.
 

[`Dot Product`](/documentation/shadergraph/math/dot-product)

 Outputs the dot product of two vectors.
 

[`Cross Product`](/documentation/shadergraph/math/cross-product)

 Calculates the cross product vector of 2 input vectors.
 

[`Transform Point`](/documentation/shadergraph/math/transform-point)

 Transforms a coordinate from one space to another.
 

[`Transform Vector`](/documentation/shadergraph/math/transform-vector)

 Transforms a vector3 from one space to another.
 

[`Transform Normal`](/documentation/shadergraph/math/transform-normal)

 Transforms a normal from one space to another.
 

[`Transform Matrix`](/documentation/shadergraph/math/transform-matrix)

 Transforms a vector by a matrix.
 

[`Transpose`](/documentation/shadergraph/math/transpose)

 Outputs the tranpose of a matrix.
 

[`Determinant`](/documentation/shadergraph/math/determinant)

 Outputs the float determinant of a matrix.
 

[`Invert Matrix`](/documentation/shadergraph/math/invert-matrix)

 Outputs the inverse of a matrix.
 

[`Rotate 2D`](/documentation/shadergraph/math/rotate-2d)

 Rotates a Vector2 (Float) about the origin in 2D.
 

[`Rotate 3D`](/documentation/shadergraph/math/rotate-3d)

 Rotates a Vector3 (Float) about a specified unit axis vector.
 

[`Place 2D`](/documentation/shadergraph/math/place-2d)

 Transforms UV texture coordinates for 2D texture placement.
 

[`Round`](/documentation/shadergraph/math/round)

 Rounds to the nearest integer value, per-channel.
 

[`Safe Power`](/documentation/shadergraph/math/safe-power)

 Raises the incoming value to an exponent and assigns the sign of the base to the output.
 

[`Normal Map`](/documentation/shadergraph/math/normal-map)

 Transforms a normal vector from object or tangent space into world space.
 

[`Fractional (Reality
  Kit)`](/documentation/shadergraph/math/fractional-(realitykit))

 Returns the fractional part of a floating point number.
 

[`One Minus (Reality
  Kit)`](/documentation/shadergraph/math/one-minus-(realitykit))

 Outputs one minus the input
 

[`Normal Map Decode`](/documentation/shadergraph/math/normal-map-decode)

 Remaps a normal’s value from [0,1] to [-1,1] by applying 2x-1.
 

