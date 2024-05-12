# environment-radiance-realitykit
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
ShaderGraph
/
 Realitykit 
/
 Environment Radiance (RealityKit) 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node
Environment Radiance (Reality
Kit)
Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.
Parameter Types
Input
Type
Base Color
Color3
Roughness
Half
Specular
Half
Metallic
Half
Normal
Vector3f
Output
Type
Diffuse Radiance
Color3
Specular Radiance
Color3
Parameter descriptions
Base Color
The base display color of the surface. The color under pure white light.
Roughness
The level of roughness of the surface. This value ranges between 
0
 and 
1
.0
, with 
0
 representing a perfectly specular surface and 
1
.0
 representing maximum roughness. The default value is 
0
.
Specular
The level of specular reflections that occur on the surface.
Metallic
The indicator if a surface is metallic or not. Set this value to 
1
 for metallic surfaces and 
0
 for nonmetallic surfaces. The default value is 
0
.0
.
Normal
The surface normal vector. The default value is 
(0,0,0)
.
Discussion:
The Environment Radiance node has two outputs:
Diffuse Radiance
The diffuse radiance of the surface. Refers to light absorbed by the surface and then re-emitted in all directions.
Specular Radiance
The specular radiance of the surface. Refers to light reflected off of the surface.
See Also
Nodes
Geometry Modifier (Reality
Kit)
A function that manipulates the location of a model’s vertices, run once per vertex.
Unlit Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Unlit material.
PBR Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Physically Based Rendering material.
Occlusion Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
Shadow Receiving Occlusion Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
View Direction (Reality
Kit)
A vector from a position in the scene to the view reference point.
Camera Position (Reality
Kit)
The position of the camera in the scene.
Geometry Modifier Model To World (Reality
Kit)
The model-to-world transformation Matrix4x4 (Float).
Geometry Modifier World To Model (Reality
Kit)
The world-to-model transformation Matrix4x4 (Float).
Geometry Modifier Normal To World (Reality
Kit)
The normal-to-world transformation Matrix3x3 (Float).
Geometry Modifier Model To View (Reality
Kit)
The model-to-view transformation Matrix4x4 (Float).
Geometry Modifier View To Projection (Reality
Kit)
The view-to-projection transformation Matrix4x4 (Float).
Geometry Modifier Projection To View (Reality
Kit)
The projection-to-view transformation Matrix4x4 (Float).
Geometry Modifier Vertex ID (Reality
Kit)
The integer index of the vertex.
Surface Model To World (Reality
Kit)
The model-to-world transformation Matrix4x4 (Float).
Surface Model To View (Reality
Kit)
The model-to-view transformation Matrix4x4 (Float).
Surface World To View (Reality
Kit)
The world-to-view transformation Matrix4x4 (Float).
Surface View To Projection (Reality
Kit)
The view-to-projection transformation Matrix4x4 (Float).
Surface Projection To View (Reality
Kit)
The projection-to-view transformation Matrix4x4 (Float).
Surface Screen Position (Reality
Kit)
The coordinates of the currently-processed data in screen space.
Surface View Direction (Reality
Kit)
A vector from a position in the scene to the view reference point.
Surface Custom Attribute (Reality
Kit)
An interpolated user-defined Vector4 (Float) data that’s from the geometry modifier.
Surface Custom Attribute 0 (vector4h)
An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
Surface Custom Attribute 1 (vector4h)
An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
Surface Custom Attribute 2 (vector4h)
An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
Surface Custom Attribute 3 (vector4h)
An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
Surface Custom Attribute 0 (vector2h)
An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
Surface Custom Attribute 1 (vector2h)
An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
Camera Index Switch (Reality
Kit)
Render different results for each eye in a stereoscopic render.
Image 2D (Reality
Kit)
A texture with RealityKit properties.
Image 2D LOD (Reality
Kit)
A texture with RealityKit properties and a explicit level of detail.
Image 2D Gradient (Reality
Kit)
A texture with RealityKit properties and a specified LOD gradient.
Image 2D Pixel (Reality
Kit)
A texture with RealityKit properties and pixel texture coordinates.
Image 2D LOD Pixel (Reality
Kit)
A texture with RealityKit properties, a explicit level of detail, and pixel texture coordinates.
Image 2D Gradient Pixel (Reality
Kit)
A texture with RealityKit properties, a specified LOD gradient, and pixel texture coordinates.
Cube Image (Reality
Kit)
A texturecube with RealityKit properties.
Cube Image LOD (Reality
Kit)
A texturecube with RealityKit properties and a explicit level of detail.
Cube Image Gradient (Reality
Kit)
A texturecube with RealityKit properties and a specified LOD gradient.
Image 2D Read (Reality
Kit)
Direct texture read.
 Current page is Environment Radiance (RealityKit) 