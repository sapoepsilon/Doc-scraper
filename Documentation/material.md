# material
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
 Material 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node Group
Material
Encapsulate a set of shader graph nodes into a single module.
Overview
Material nodes help you divide your graph into subsets of nodes, each with distinct inputs and outputs. A 
Node
Graph
 appears as a single node within your main graph. Editing that node hides the main graph and gives you an empty space that you can fill with additional nodes. Use that space to build a specific portion of your main graph, and use the 
Node
Graph
 to define the inputs and outputs to that separate space.
Topics
Nodes
Node
Graph
A node that can contain shading nodes and other node graphs.
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
Geometric
Access scene geometry while your graph runs.
Logic
Perform Boolean operations and other logical comparisons on data values.
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
 Current page is Material 