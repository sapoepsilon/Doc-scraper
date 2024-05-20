# geometry-modifier-realitykit


[Parameter Types](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)#Parameter-Types)
-------------------------------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Model Position Offset` | Vector3f |
| `Color` | Color4 |
| `Normal` | Vector3f |
| `Bitangent` | Vector3f |
| `Uv0` | Vector2f |
| `Uv1` | Vector2f |
| `User Attribute` | Vector4f |
| `User Attribute Half4 0` | Vector4h |
| `User Attribute Half4 1` | Vector4h |
| `User Attribute Half4 2` | Vector4h |
| `User Attribute Half4 3` | Vector4h |
| `User Attribute Half2 0` | Vector2h |
| `User Attribute Half2 1` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Token |

[Parameter descriptions](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)#Parameter-descriptions)
---------------------------------------------------------------------------------------------------------------------

`Model Position Offset` 

 The offset to each vertices model position.
 

`Color` 

 The color of each vertex.
 

`Normal` 

 The normal vector for each vertex.
 

`Bitangent` 

 The bitangent vector for each vertex.
 

`Uv0` 

 A set of texture coordinates for each vertex.
 

`Uv1` 

 A set of texture coordinates for each vertex.
 

`User Attribute` 

 A user-defined attribute to apply to each vertex of the object.
 

`User Attribute Half4 0` 

 A user-defined attribute the node attaches to each vertex of the object.
 

`User Attribute Half4 1` 

 A user-defined attribute the node attaches to each vertex of the object.
 

`User Attribute Half4 2` 

 A user-defined attribute the node attaches to each vertex of the object.
 

`User Attribute Half4 3` 

 A user-defined attribute the node attaches to each vertex of the object.
 

`User Attribute Half2 0` 

 A user-defined attribute the node attaches to each vertex of the object.
 

`User Attribute Half2 1` 

 A user-defined attribute the node attaches to each vertex of the object.
 

[Discussion](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)#Discussion)
---------------------------------------------------------------------------------------------

 The Geometry Modifier node can be used to cause a material to affect the geometry of any object to which it’s applied, in addition to the objects texture. Connect the output of the Geometry modifier node to the
 `Custom Geometry Modifier` 
 output of your material. Below is an example of a simple node graph that uses the Geometry Modifier node to alter the
 *Y* 
 model positions of vertices.
 

![](https://docs-assets.developer.apple.com/published/00136a30e1f473e17c13809511e24380/GeometryModifierGraph.png)

 Use the Noise 2D node to procedurally generate an amount to offset the
 *Y* 
 position of each vertex. You can also use the noise to add shadows to the texture in order to show the change in model position more clearly. Below, the resulting material applies to a plane.
 

![](https://docs-assets.developer.apple.com/published/4a79a93ee45909df54677e2f4490b485/GeometryModifierMaterial1.png)

 Object before modifier
 

![](https://docs-assets.developer.apple.com/published/6372214cee3c7c81eb2f6c578db4c62c/GeometryModifierMaterial2.png)

 Object after modifier
 

 A function that manipulates the location of a model’s vertices, run once per vertex.

[See Also](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)#see-also)
-----------------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)#nodes)

[`Unlit Surface (Reality
  Kit)`](/documentation/shadergraph/realitykit/unlit-surface-(realitykit))

 A surface shader that defines properties for a RealityKit Unlit material.
 

[`PBR Surface (Reality
  Kit)`](/documentation/shadergraph/realitykit/pbr-surface-(realitykit))

 A surface shader that defines properties for a RealityKit Physically Based Rendering material.
 

[`Occlusion Surface (Reality
  Kit)`](/documentation/shadergraph/realitykit/occlusion-surface-(realitykit))

 A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
 

[`Shadow Receiving Occlusion Surface (Reality
  Kit)`](/documentation/shadergraph/realitykit/shadow-receiving-occlusion-surface-(realitykit))

 A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
 

[`View Direction (Reality
  Kit)`](/documentation/shadergraph/realitykit/view-direction-(realitykit))

 A vector from a position in the scene to the view reference point.
 

[`Camera Position (Reality
  Kit)`](/documentation/shadergraph/realitykit/camera-position-(realitykit))

 The position of the camera in the scene.
 

[`Geometry Modifier Model To World (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-model-to-world-(realitykit))

 The model-to-world transformation Matrix4x4 (Float).
 

[`Geometry Modifier World To Model (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-world-to-model-(realitykit))

 The world-to-model transformation Matrix4x4 (Float).
 

[`Geometry Modifier Normal To World (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-normal-to-world-(realitykit))

 The normal-to-world transformation Matrix3x3 (Float).
 

[`Geometry Modifier Model To View (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-model-to-view-(realitykit))

 The model-to-view transformation Matrix4x4 (Float).
 

[`Geometry Modifier View To Projection (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-view-to-projection-(realitykit))

 The view-to-projection transformation Matrix4x4 (Float).
 

[`Geometry Modifier Projection To View (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-projection-to-view-(realitykit))

 The projection-to-view transformation Matrix4x4 (Float).
 

[`Geometry Modifier Vertex ID (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-vertex-id-(realitykit))

 The integer index of the vertex.
 

[`Surface Model To World (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-model-to-world-(realitykit))

 The model-to-world transformation Matrix4x4 (Float).
 

[`Surface Model To View (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-model-to-view-(realitykit))

 The model-to-view transformation Matrix4x4 (Float).
 

[`Surface World To View (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-world-to-view-(realitykit))

 The world-to-view transformation Matrix4x4 (Float).
 

[`Surface View To Projection (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-view-to-projection-(realitykit))

 The view-to-projection transformation Matrix4x4 (Float).
 

[`Surface Projection To View (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-projection-to-view-(realitykit))

 The projection-to-view transformation Matrix4x4 (Float).
 

[`Surface Screen Position (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-screen-position-(realitykit))

 The coordinates of the currently-processed data in screen space.
 

[`Surface View Direction (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-view-direction-(realitykit))

 A vector from a position in the scene to the view reference point.
 

[`Surface Custom Attribute (Reality
  Kit)`](/documentation/shadergraph/realitykit/surface-custom-attribute-(realitykit))

 An interpolated user-defined Vector4 (Float) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 0 (vector4h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-0-(vector4h))

 An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 1 (vector4h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-1-(vector4h))

 An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 2 (vector4h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-2-(vector4h))

 An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 3 (vector4h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-3-(vector4h))

 An interpolated user-defined Vector4 (Half) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 0 (vector2h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-0-(vector2h))

 An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
 

[`Surface Custom Attribute 1 (vector2h)`](/documentation/shadergraph/realitykit/surface-custom-attribute-1-(vector2h))

 An interpolated user-defined Vector2 (Half) data that’s from the geometry modifier.
 

[`Environment Radiance (Reality
  Kit)`](/documentation/shadergraph/realitykit/environment-radiance-(realitykit))

 Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.
 

[`Camera Index Switch (Reality
  Kit)`](/documentation/shadergraph/realitykit/camera-index-switch-(realitykit))

 Render different results for each eye in a stereoscopic render.
 

[`Image 2D (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-(realitykit))

 A texture with RealityKit properties.
 

[`Image 2D LOD (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-lod-(realitykit))

 A texture with RealityKit properties and a explicit level of detail.
 

[`Image 2D Gradient (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-gradient-(realitykit))

 A texture with RealityKit properties and a specified LOD gradient.
 

[`Image 2D Pixel (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-pixel-(realitykit))

 A texture with RealityKit properties and pixel texture coordinates.
 

[`Image 2D LOD Pixel (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-lod-pixel-(realitykit))

 A texture with RealityKit properties, a explicit level of detail, and pixel texture coordinates.
 

[`Image 2D Gradient Pixel (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-gradient-pixel-(realitykit))

 A texture with RealityKit properties, a specified LOD gradient, and pixel texture coordinates.
 

[`Cube Image (Reality
  Kit)`](/documentation/shadergraph/realitykit/cube-image-(realitykit))

 A texturecube with RealityKit properties.
 

[`Cube Image LOD (Reality
  Kit)`](/documentation/shadergraph/realitykit/cube-image-lod-(realitykit))

 A texturecube with RealityKit properties and a explicit level of detail.
 

[`Cube Image Gradient (Reality
  Kit)`](/documentation/shadergraph/realitykit/cube-image-gradient-(realitykit))

 A texturecube with RealityKit properties and a specified LOD gradient.
 

[`Image 2D Read (Reality
  Kit)`](/documentation/shadergraph/realitykit/image-2d-read-(realitykit))

 Direct texture read.
 

