# normal-map


[Parameter Types](/documentation/shadergraph/math/normal-map#Parameter-Types)
-----------------------------------------------------------------------------

* [Normal Map](#)
* [Normal Map (vector2f Scale)](#)

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Space` | String |
| `Scale` | Float |
| `Normal` | Vector3f |
| `Tangent` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Space` | String |
| `Scale` | Vector2f |
| `Normal` | Vector3f |
| `Tangent` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/math/normal-map#Parameter-descriptions)
-------------------------------------------------------------------------------------------

`In` 

 The input vector to be transformed. The default value is
 `(0
 
 .5, 0
 
 .5, 1
 
 .0)` 
 .
 

`Space` 

 The space from which the node transforms the normal vector. The value can either be
 `object` 
 or
 `tangent` 
 . The default value is
 `tangent` 
 .
 

`Scale` 

 A scalar multiplier for the input vector before the node transforms it. The default value is
 `1
 
 .0` 
 .
 

`Normal` 

 The surface normal vector. The default value is the current surface normal of world space.
 

`Tangent` 

 The surface tangent vector. The default value is the current tangent vector of world space.
 

 Transforms a normal vector from object or tangent space into world space.

[See Also](/documentation/shadergraph/math/normal-map#see-also)
---------------------------------------------------------------

### [Nodes](/documentation/shadergraph/math/normal-map#nodes)

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
 

[`Fractional (Reality
  Kit)`](/documentation/shadergraph/math/fractional-(realitykit))

 Returns the fractional part of a floating point number.
 

[`One Minus (Reality
  Kit)`](/documentation/shadergraph/math/one-minus-(realitykit))

 Outputs one minus the input
 

[`Normal Map Decode`](/documentation/shadergraph/math/normal-map-decode)

 Remaps a normal’s value from [0,1] to [-1,1] by applying 2x-1.
 

