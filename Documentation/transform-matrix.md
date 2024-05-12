# transform-matrix
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
ShaderGraph
/
 Math 
/
 Transform Matrix 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node
Transform Matrix
Transforms a vector by a matrix.
Parameter Types
 Transform Matrix (vector2f matrix3x3f) 
 Transform Matrix (vector3f) 
 Transform Matrix (vector2f) 
 Transform Matrix (vector4f) 
 Transform Matrix (vector3f matrix4x4f) 
Input
Type
In
Vector2f
Mat
Matrix3x3f
Output
Type
Out
Vector2f
Input
Type
In
Vector3f
Mat
Matrix3x3f
Output
Type
Out
Vector3f
Input
Type
In
Vector2f
Mat
Matrix2x2f
Output
Type
Out
Vector2f
Input
Type
In
Vector4f
Mat
Matrix4x4f
Output
Type
Out
Vector4f
Input
Type
In
Vector3f
Mat
Matrix4x4f
Output
Type
Out
Vector3f
Parameter descriptions
In
The vector to transform. This node appends an addtional component onto the 
In
 vector with a value of 
1
.0
 to make the vector match the dimensions of the 
Mat
 matrix. This additional compenent is removed after the transformation completes.
Mat
The matrix by which to transform the 
In
 vector. The default value is the identity matrix.
See Also
Nodes
Add
Adds two values.
Subtract
Subtracts two values.
Multiply
Multiplies two values.
Divide
Divides two values.
Modulo
Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
Abs
Outputs the per-channel absolute value of the input.
Floor
Outputs the nearest integer value, per-channel, less than or equal to the incoming values.
Ceiling
Outputs the nearest integer value, per-channel, greater than or equal to the incoming values.
Power
Raises the incoming value to an exponent.
Sin
The sine of the incoming value in radians.
Cos
The cosine of the incoming value in radians.
Tan
The tangent of the incoming value in radians.
Asin
The arcsine of the incoming value in radians.
Acos
The arccosine of the incoming value in radians.
Atan2
The arctangent of the expression (iny/inx) in radians.
Square Root
The square root of the incoming value.
Natural Log
The natural log of the input.
Exp
Outputs ‘e’ to the power of the input.
Sign
The per-channel sign of the input value: -1 for negative, +1 for positive, 0 for zero.
Clamp
Clamps the input per-channel to a specified range.
Min
Outputs the minimum of two incoming values.
Max
Outputs the maximum of two incoming values.
Normalize
Outputs a normalized vector.
Magnitude
Outputs the float magnitude of a vector.
Dot Product
Outputs the dot product of two vectors.
Cross Product
Calculates the cross product vector of 2 input vectors.
Transform Point
Transforms a coordinate from one space to another.
Transform Vector
Transforms a vector3 from one space to another.
Transform Normal
Transforms a normal from one space to another.
Transpose
Outputs the tranpose of a matrix.
Determinant
Outputs the float determinant of a matrix.
Invert Matrix
Outputs the inverse of a matrix.
Rotate 2D
Rotates a Vector2 (Float) about the origin in 2D.
Rotate 3D
Rotates a Vector3 (Float) about a specified unit axis vector.
Place 2D
Transforms UV texture coordinates for 2D texture placement.
Round
Rounds to the nearest integer value, per-channel.
Safe Power
Raises the incoming value to an exponent and assigns the sign of the base to the output.
Normal Map
Transforms a normal vector from object or tangent space into world space.
Fractional (Reality
Kit)
Returns the fractional part of a floating point number.
One Minus (Reality
Kit)
Outputs one minus the input
Normal Map Decode
Remaps a normal’s value from [0,1] to [-1,1] by applying 2x-1.
 Current page is Transform Matrix 