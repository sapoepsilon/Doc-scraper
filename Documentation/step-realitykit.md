# step-realitykit
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
ShaderGraph
/
 Adjustment 
/
 Step (RealityKit) 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node
Step (Reality
Kit)
Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.
Parameter Types
 Step (float) 
 Step (color3f) 
 Step (color4f) 
 Step (vector3f) 
 Step (vector4f) 
 Step (vector2f) 
Input
Type
In
Float
Edge
Float
Output
Type
Out
Float
Input
Type
In
Color3
Edge
Color3
Output
Type
Out
Color3
Input
Type
In
Color4
Edge
Color4
Output
Type
Out
Color4
Input
Type
In
Vector3f
Edge
Vector3f
Output
Type
Out
Vector3f
Input
Type
In
Vector4f
Edge
Vector4f
Output
Type
Out
Vector4f
Input
Type
In
Vector2f
Edge
Vector2f
Output
Type
Out
Vector2f
Parameter descriptions
In
The input value.
Edge
The deciding value to which to compare the input.
Discussion
The Step node takes the 
In
 value and compares it to the 
Edge
 parameter. If the value is less than 
Edge
, the node returns 
0
. Otherwise, it returns 
1
.
See Also
Nodes
Remap
Linearly remaps incoming values from one range to another.
Smooth Step
Outputs a smooth remapping from low-high to 0-1.
Luminance
Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.
RGB to HSV
Converts a color from RGB to HSV space.
HSV to RGB
Converts a color from HSV to RGB space.
Contrast
Increases or decreases contrast of values using a linear slope multiplier.
Range
Remaps incoming values from one range to another.
HSV Adjust
Adjusts the hue, saturation and value of an RGB color by a vector .
Saturate
Adjusts the saturation of a color.
 Current page is Step (RealityKit) 