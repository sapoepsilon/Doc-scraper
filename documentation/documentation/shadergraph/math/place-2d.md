# place-2d


[Parameter Types](/documentation/shadergraph/math/place-2d#Parameter-Types)
---------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |
| `Pivot` | Vector2f |
| `Scale` | Vector2f |
| `Rotate` | Float |
| `Offset` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

[Parameter descriptions](/documentation/shadergraph/math/place-2d#Parameter-descriptions)
-----------------------------------------------------------------------------------------

`Texture Coordinates` 

 The input texture coordinates to transform. The default value is the current surface texture coordinates with an index of
 `0` 
 .
 

`Pivot` 

 The pivot point for scaling and rotating the texture coordinates. The node subtracts this value from
 *U* 
 and
 *V* 
 before it applies the scale or rotation. The node then adds this value back later.
 

`Scale` 

 The value by which to scale the texture coordinates. The node divides the
 *U* 
 and
 *V* 
 coordinates by this value. The default value is
 `(1,1)` 

`Rotate` 

 The number of degrees to rotate the texture coordinates. A postive value rotates the texture coordinates by that many degrees counter-clockwise and the resulting image clockwise. A negative value rotates the texture coordinates by that many degrees clockwise and the resulting image counter-clockwise. The default value is
 `0` 
 .
 

`Offset` 

 The value to offset the postion of the texture coordinates. The node subtracts this value from the texture coordinates after it has been scaled, rotated, and the pivot has been added back. The default value is
 `(0,0)` 
 .
 

[Discussion](/documentation/shadergraph/math/place-2d#Discussion)
-----------------------------------------------------------------

 The Place 2D node can be used to transform texture coordinates and apply these basic transformations to textures. Below is an example of a simple node graph that uses the Place 2D Node to transform texture coordinates that are then passed to an image node.
 

![](https://docs-assets.developer.apple.com/published/9eedcf2c05258008ef6543a7b5d1d075/Place2dGraph.png)

 The incoming texture coordinates are transformed in three ways. They are scaled down to half the size, rotated 180 degrees, and offset by 0.5 in both the
 *U* 
 and
 *V* 
 direction. For the scale and rotation, the pivot point is set to
 `(0
 
 .5, 0
 
 .5)` 
 . Because texture coordinates generally range from
 `(0-1)` 
 this means the scale and rotation are done from the center point of the image. Below is the original image and the texture with the transformation applied.
 

![](https://docs-assets.developer.apple.com/published/78717aea759b374d62a6c56468ba269e/Place2dMaterial1.png)

 Original Image
 

![](https://docs-assets.developer.apple.com/published/efc54695250fd8a7151a87eab115b4f3/Place2dMaterial2.png)

 Image after transformations
 

 Transforms UV texture coordinates for 2D texture placement.

[See Also](/documentation/shadergraph/math/place-2d#see-also)
-------------------------------------------------------------

### [Nodes](/documentation/shadergraph/math/place-2d#nodes)

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
 

