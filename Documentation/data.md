# data
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
 Data 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node Group
Data
Convert data values to different formats, or manipulate individual elements within a data structure.
Overview
Use data nodes to take one type of data and manipulate it to get a different type of value. Data manipulations can take several forms:
Convert one data type to a different format.
Combine individual elements to create a single data type.
Separate a single data type into its component elements.
Extract or manipulate individual values from a data structure and use them as input to other nodes.
Topics
Nodes
Convert
Converts a stream from one data type to another.
Swizzle
Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
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
See Also
Node Categories
2D-Procedural
Generate 2D gradients, noise, and other patterns programmatically for your material.
2D-Texture
Load and configure 2D texture files.
3D-Procedural
Generate 3D noise patterns programmatically for your material.
3D-Texture
Project multiple 2D images onto a surface to create a 3D texture.
Adjustment
Modify or convert values, or ranges of values, from one form to another.
Application
Get system values such as the current time or the direction of the up vector.
Compositing
Generate a single output from the combination of multiple data values.
Geometric
Access scene geometry while your graph runs.
Logic
Perform Boolean operations and other logical comparisons on data values.
Material
Encapsulate a set of shader graph nodes into a single module.
Math
Perform a wide variety of mathematical and transformative operations on data values.
Organization
Modify the visual flow of data within your graph without changing any values.
Procedural
Add a constant number, vector, matrix, color, string, or other value to your graph.
Realitykit
Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.
Surface
Generate a MaterialX preview surface.
 Current page is Data 