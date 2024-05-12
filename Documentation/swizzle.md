# swizzle
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
ShaderGraph
/
 Data 
/
 Swizzle 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node
Swizzle
Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
Parameter Types
 Swizzle (float color3f) 
 Swizzle (color4f color4f) 
 Swizzle (color4f color3f) 
 Swizzle (half color3f) 
 Swizzle (half vector2h) 
 Swizzle (vector2f vector3f) 
 Swizzle (vector3f float) 
 Swizzle (vector4f vector4f) 
 Swizzle (color3f half) 
 Swizzle (float vector2f) 
 Swizzle (vector4f color4f) 
 Swizzle (vector4f vector3f) 
 Swizzle (vector2f color4f) 
 Swizzle (vector3f vector2f) 
 Swizzle (vector4f float) 
 Swizzle (vector4f color3f) 
 Swizzle (color3f color4f) 
 Swizzle (half color4f) 
 Swizzle (color4f vector2f) 
 Swizzle (float vector4f) 
 Swizzle (vector4f half) 
 Swizzle (vector2f vector2f) 
 Swizzle (float color4f) 
 Swizzle (vector3f color3f) 
 Swizzle (color3f vector4f) 
 Swizzle (vector3f color4f) 
 Swizzle (half vector3h) 
 Swizzle (vector4f vector2f) 
 Swizzle (vector3f half) 
 Swizzle (color3f vector3f) 
 Swizzle (color3f float) 
 Swizzle (vector2f color3f) 
 Swizzle (vector3f vector3f) 
 Swizzle (vector3f vector4f) 
 Swizzle (color4f half) 
 Swizzle (vector2f vector4f) 
 Swizzle (color3f color3f) 
 Swizzle (vector2f half) 
 Swizzle (half vector4h) 
 Swizzle (vector2f float) 
 Swizzle (color4f float) 
 Swizzle (color4f vector3f) 
 Swizzle (color4f vector4f) 
 Swizzle (color3f vector2f) 
 Swizzle (float vector3f) 
Input
Type
In
Float
Channels
String
Output
Type
Out
Color3
Input
Type
In
Color4
Channels
String
Output
Type
Out
Color4
Input
Type
In
Color4
Channels
String
Output
Type
Out
Color3
Input
Type
In
Half
Channels
String
Output
Type
Out
Color3
Input
Type
In
Half
Channels
String
Output
Type
Out
Vector2h
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Vector3f
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Float
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Color3
Channels
String
Output
Type
Out
Half
Input
Type
In
Float
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Color4
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Vector3f
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Color4
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Float
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Color3
Input
Type
In
Color3
Channels
String
Output
Type
Out
Color4
Input
Type
In
Half
Channels
String
Output
Type
Out
Color4
Input
Type
In
Color4
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Float
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Half
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Float
Channels
String
Output
Type
Out
Color4
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Color3
Input
Type
In
Color3
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Color4
Input
Type
In
Half
Channels
String
Output
Type
Out
Vector3h
Input
Type
In
Vector4f
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Half
Input
Type
In
Color3
Channels
String
Output
Type
Out
Vector3f
Input
Type
In
Color3
Channels
String
Output
Type
Out
Float
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Color3
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Vector3f
Input
Type
In
Vector3f
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Color4
Channels
String
Output
Type
Out
Half
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Color3
Channels
String
Output
Type
Out
Color3
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Half
Input
Type
In
Half
Channels
String
Output
Type
Out
Vector4h
Input
Type
In
Vector2f
Channels
String
Output
Type
Out
Float
Input
Type
In
Color4
Channels
String
Output
Type
Out
Float
Input
Type
In
Color4
Channels
String
Output
Type
Out
Vector3f
Input
Type
In
Color4
Channels
String
Output
Type
Out
Vector4f
Input
Type
In
Color3
Channels
String
Output
Type
Out
Vector2f
Input
Type
In
Float
Channels
String
Output
Type
Out
Vector3f
Parameter descriptions
In
The input value
Channels
A string of 
1-4
 characters that determine the permutation to perform. These characters can be “r”, “g”, “b”, or “a” if the 
In
 parameter is a color input, or “x”, “y”, “z”, or “w” for vector inputs. Use “r” or “x” if the input is a float.
Discussion
The Swizzle node determines its output by first looking at the 
Channels
 parameter. Each character in the 
Channel
 string represents one of the channels of the 
In
 parameter. For example, if you pass in a vector3 of 
(1, 5, 10)
 as the 
In
 parameter, “x” refers to 
1
, “y” to 
5
, and “z” to 
10
. The order of the characters determines how the channels of the input switch around to create the output. For the previous example, if the 
Channels
 parameter is “zzz”, the output is 
(10, 10, 10)
.
Note
The number of characters in the 
Channels
 must be equal to the number of channels in the output.
The table below shows additional examples of the swizzle node process.
In
Channels
Out
Vector3: (1, 5, 10)
zzz
Vector3: (10, 10, 10)
Vector3: (1, 5, 10)
zyx
Vector3: (10, 5, 1)
Vector2: (5, 0)
xxy
Vector3: (5, 5, 0)
Vector3: (1, 5, 10)
zx
Vector2: (10, 1)
Color3: (0.5, 0.8, 0)
grb
Color3: (0.8, 0.5, 0)
See Also
Nodes
Convert
Converts a stream from one data type to another.
Combine 2
Combines the channels from two streams into two channels of a single output stream of a compatible type.
Combine 3
Combines the channels from three streams into three channels of a single output stream of a compatible type.
Combine 4
Combines the channels from four streams into four channels of a single output stream of a compatible type.
Extract
Generates a float stream from one channel of a color​N o​r vector​N ​stream.
Separate 2
Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.
Separate 3
Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
Separate 4
Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
Primvar Reader (integer)
A node that provides the ability for shading networks to consume integer data defined on geometry.
Primvar Reader (bool)
A node that provides the ability for shading networks to consume boolean data defined on geometry.
Primvar Reader (float)
A node that provides the ability for shading networks to consume float data defined on geometry.
Primvar Reader (vector2f)
A node that provides the ability for shading networks to consume float2 data defined on geometry.
Primvar Reader (vector3f)
A node that provides the ability for shading networks to consume float3 data defined on geometry.
Primvar Reader (vector4f)
A node that provides the ability for shading networks to consume float4 data defined on geometry.
 Current page is Swizzle 