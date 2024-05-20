# multiply


[Parameter Types](/documentation/shadergraph/math/multiply#Parameter-Types)
---------------------------------------------------------------------------

* [Multiply (float)](#)
* [Multiply (Displacement Shader V)](#)
* [Multiply (matrix2x2f)](#)
* [Multiply (vector3f \* float)](#)
* [Multiply (vector2f \* float)](#)
* [Multiply (vector3f)](#)
* [Multiply (Displacement Shader F)](#)
* [Multiply (color3f)](#)
* [Multiply (vector4f \* float)](#)
* [Multiply (matrix4x4f)](#)
* [Multiply (matrix3x3f)](#)
* [Multiply (vector4f)](#)
* [Multiply (color4f \* float)](#)
* [Multiply (half)](#)
* [Multiply (Surface Shader F)](#)
* [Multiply (color4f)](#)
* [Multiply (color3f \* float)](#)
* [Multiply (vector2f)](#)

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In 1` | Token |
| `In 2` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Token |

| Input | Type |
| --- | --- |
| `In 1` | Matrix2x2f |
| `In 2` | Matrix2x2f |

| Output | Type |
| --- | --- |
| `Out` | Matrix2x2f |

| Input | Type |
| --- | --- |
| `In 1` | Vector3f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In 1` | Vector2f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In 1` | Vector3f |
| `In 2` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In 1` | Token |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Token |

| Input | Type |
| --- | --- |
| `In 1` | Color3 |
| `In 2` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In 1` | Vector4f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In 1` | Matrix4x4f |
| `In 2` | Matrix4x4f |

| Output | Type |
| --- | --- |
| `Out` | Matrix4x4f |

| Input | Type |
| --- | --- |
| `In 1` | Matrix3x3f |
| `In 2` | Matrix3x3f |

| Output | Type |
| --- | --- |
| `Out` | Matrix3x3f |

| Input | Type |
| --- | --- |
| `In 1` | Vector4f |
| `In 2` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In 1` | Color4 |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In 1` | Half |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In 1` | Token |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Token |

| Input | Type |
| --- | --- |
| `In 1` | Color4 |
| `In 2` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In 1` | Color3 |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In 1` | Vector2f |
| `In 2` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

 Multiplies two values.

[See Also](/documentation/shadergraph/math/multiply#see-also)
-------------------------------------------------------------

### [Nodes](/documentation/shadergraph/math/multiply#nodes)

[`Add`](/documentation/shadergraph/math/add)

 Adds two values.
 

[`Subtract`](/documentation/shadergraph/math/subtract)

 Subtracts two values.
 

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
 

[`Clamp`](/documentation/shadergraph/math/clamp)

 Clamps the input per-channel to a specified range.
 

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
 

