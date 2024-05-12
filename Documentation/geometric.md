# geometric
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
 Geometric 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node Group
Geometric
Access scene geometry while your graph runs.
Overview
When the GPU applies your graph to a scene, geometric nodes reflect the data value the system is currently processing. Use these nodes to get details about that data value, such as its coordinates, normal, or tangent information. Alternatively, use the Reflect and Refract nodes to modify vectors relative to the current data value.
Topics
Nodes
Position
The coordinates of the currently-processed data in a given coordinate space.
Normal
The geometric normal of the currently-processed data in a given coordinate space.
Tangent
The geometric tangent of the currently-processed data in a given coordinate space.
Bitangent
The geometric bitangent vector of the currently-processed data in a given coordinate space.
Texture Coordinates
The 2D or 3D texture coordinates of the currently-processed data.
Geometry Color
The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
Geometric Property
The value of the specified geometric property (defined using ) of the currently-bound geometry.
Reflect (Reality
Kit)
Reflects a vector about another vector.
Refract (Reality
Kit)
Refracts a vector using a given normal and index of refraction (eta).
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
Data
Convert data values to different formats, or manipulate individual elements within a data structure.
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
 Current page is Geometric 