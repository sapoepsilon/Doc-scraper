# pbr-surface-realitykit
 Documentation 
 Open Menu 
/
 ShaderGraph 
/
ShaderGraph
/
 Realitykit 
/
 PBR Surface (RealityKit) 
Swift
Language: 
Swift
 API Changes: 
None
ShaderGraph Node
PBR Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Physically Based Rendering material.
Parameter Types
Input
Type
Base Color
Color3
Emissive Color
Color3
Normal
Vector3f
Roughness
Float
Metallic
Float
Ambient Occlusion
Float
Specular
Float
Opacity
Float
Opacity Threshold
Float
Clearcoat
Float
Clearcoat Roughness
Float
Has Premultiplied Alpha
Bool
Output
Type
Out
Token
Parameter descriptions
Base Color
The base display color of the surface. The color of an object under pure white light.
Emissive Color
The self-illumination color of the surface. The color the surface displays as if it is self-lit.
Normal
The normal vector in tangent space. The default value is 
(0,0,1)
.
Roughness
The level of roughness of the surface. This value ranges between 
0
 and 
1
.0
, with 
0
 outputting a perfectly specular surface and 
1
.0
 indicating maximum roughness. The default value is 
0
.5
.
Metallic
Indicates if a surface is metallic or not. Set this value to 
1
 for metallic surfaces and 
0
 for nonmetallic surfaces. The default value is 
0
.0
.
Ambient Occlusion
The degree of ambient lighting that the surface receives. This value simulates soft shadows and subtle shading.
Specular
The brightness of the specular highlight of the material.
Opacity
The level of opaqueness of the surface. If the value of this parameter is 
1
.0
, the surface is fully opaque. If the value is less than 
1
.0
, the surface appears translucent. If the value is 
0
, the surface is completely transparent. The default value is 
1
.0
.
Opacity Threshold
The threshold for whether a portion of the surface is rendered based on its opacity level. A value of 
0
.0
 means that no additional masking occurs. If the value is greater than 
0
.0
, the node renders only areas of the surface with an 
Opacity
 value greater than the value of this parameter. This parameter can be enabled or disabled. The default value is 
0
.0
.
Clearcoat
A second clear reflective layer on the surface. This property produces a glossy finish. The default value is 
0
.0
.
Clearcoat Roughness
The level of roughness of the surfaces clearcoat layer. The default value is 
0
.01
.
Has Premultiplied Alpha
A Boolean to let the node know if input parameters have a premultiplied alpha.
Discussion
The PBR Surface node produces a custom surface based on its input parameters. Connect the output of the PBR Surface node to the 
Custom Surface
 output of your material.
Below is an example material that uses only the PBR Surface node to produce a gold-like texture and apply it to a sphere.
See Also
Nodes
Geometry Modifier (Reality
Kit)
A function that manipulates the location of a model’s vertices, run once per vertex.
Unlit Surface (Reality
Kit)
A surface shader that defines properties for a RealityKit Unlit material.
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
Environment Radiance (Reality
Kit)
Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.
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
 Current page is PBR Surface (RealityKit) 