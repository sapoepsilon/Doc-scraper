# image-2d-realitykit


[Parameter Types](/documentation/shadergraph/realitykit/image-2d-(realitykit)#Parameter-Types)
----------------------------------------------------------------------------------------------

* [Image 2D (vector4)](#)
* [Image 2D (color4)](#)
* [Image 2D (color3)](#)

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Vector4f |
| `Texture Coordinates` | Vector2f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer2 |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Color4 |
| `Texture Coordinates` | Vector2f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer2 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Color3 |
| `Texture Coordinates` | Vector2f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer2 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

[Parameter descriptions](/documentation/shadergraph/realitykit/image-2d-(realitykit)#Parameter-descriptions)
------------------------------------------------------------------------------------------------------------

`File` 

 The image file to use for the texture.
 

`U Wrap Mode` 

 The way the node handles
 *U* 
 values outside of the range of
 `0-1` 
 . The default value is
 `clamp
 
 _to
 
 _edge` 
 .
 

`V Wrap Mode` 

 The way the node handles
 *V* 
 values outside of the range of
 `0-1` 
 . The default value is
 `clamp
 
 _to
 
 _edge` 
 .
 

`Border Color` 

 A color that fills in areas of a material’s surface not covered by the material property’s image contents. The default value is
 `transparent
 
 _black` 
 .
 

`Mag Filter` 

 The magnification filtering mode the node uses to render the image contents at a size larger than the original image. For example, the texture coordinates at a point near the camera may correspond to a small fraction of a pixel in the texture image. This node uses the
 `Mag Filter` 
 to determine the color of the sampled texel at that point. The default value is
 `linear` 
 .
 

`Min Filter` 

 The minimizing filtering mode the node uses to render the image contents at a size smaller than the original image. For example, the texture coordinates at a point far from the camera may correspond to an area of several pixels in the texture image. This node uses the
 `Min Filter` 
 to determine the color of the sampled texel at that point. The default value is
 `linear` 
 .
 

`Mip Filter` 

 The mipmap filtering mode the node uses when rendering the image contents using mipmapping. Useful when rendering an image at a size smaller than the original image. If the value of this parameter is
 `None` 
 , the node won’t use mipmapping. The default value is
 `linear` 
 .
 

`Max Anisotropy` 

 The amount of anisotropic texture filtering applied when rendering the texture’s image contents. Used when rendering the image contents at an extreme angle relative to the camera. This parameter is used only in conjunction with mipmapping, so it only has an effect if
 `Mip Filter` 
 isn’t
 `None` 
 . The default value is
 `1` 
 .
 

`Max Lod Clamp` 

 The maximum level of detail allowed for the rendered image contents. As an object gets closer to the camera, the level of detail used to render the texture of that object increases up to the maximum defined by this parameter. The default value is
 `65504` 
 .
 

`Min Lod Clamp` 

 The minimum level of detail allowed for the rendered image contents. As an object gets farther from the camera, the level of detail used to render the texture of that object decreases to the minimum defined by this parameter. The default value is
 `0` 
 .
 

`Default` 

 The default value to use if the ​
 `File​` 
 parameter fails to resolve.
 

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

`Bias` 

 The bias for the level of detail of the rendered image contents. When the size of the rendered texture is between two LOD levels, this parameter weights the choice of which level the renderer uses toward either the more detailed level or the less detailed level. When the value is between
 `0` 
 and
 `1` 
 , the node favors less detail. If the value is greater than
 `1` 
 , the node favors more detail. The default value is
 `0` 
 .
 

`Dynamic Min Lod Clamp` 

 The minimum level of detail allowed for the rendered image contents. Similar to the
 `Min Lod Clamp` 
 parameter, except this parameter may be changed dynamically during runtime, while the
 `Min Lod Clamp` 
 parameter can’t.
 

`Offset` 

 The integer values added to the texture coordinates before looking up each pixel. The value must be within the range
 `-8-7` 
 . The default value is
 `0` 
 .
 

[Discussion](/documentation/shadergraph/realitykit/image-2d-(realitykit)#Discussion)
------------------------------------------------------------------------------------

 The Image 2D node produces a texture using the contents of the image file specified in the
 `File` 
 parameter. It has a multitude of parameters that affect the properties of the rendered textures.
 

 For the wrap mode parameters, the possible values are:
 

`clamp
 
 _to
 
 _border` 

 The node sets texture coordinates outside the normal range to the color specified by the
 `Border Color` 
 parameter.
 

`clamp
 
 _to
 
 _edge` 

 The node clamps texture coordinates outside the normal range to the normal range. The node will set any values greater than
 `1` 
 to
 `1` 
 , and any values less than
 `0` 
 to
 `0` 
 . This means the color’s on the edge of the image will extend to fill the rest of the texture.
 

`clamp
 
 _to
 
 _zero` 

 The node sets texture coordinates outside the normal range to a color of value of
 `0` 
 or black. This is equivalent to the
 `clamp
 
 _to
 
 _border` 
 option with a border color of
 `transparent
 
 _black` 
 .
 

`mirrored
 
 _repeat` 

 The node mirrors texture coordinates outside the normal range.
 

`repeat` 

 The node will cause texture coordinates outside the normal range to “wrap around.” This behavior is effectively equivalent to the node applying modulo 1 to the coordinates.
 

 Warning
 

 You can only use the clamp-to-zero option if the
 `Border Color` 
 parameter is set to
 `transparent
 
 _black` 
 ; otherwise, the behavior of the node is undefined.
 

 For the
 `Mag Filter` 
 and
 `Min Filter` 
 parameters, the possible values are:
 

`linear` 

 The filter uses linear interpolation of the closest values in order to determine the rendered contents.
 

`nearest` 

 The filter uses the nearest value in order to determine the rendered contents.
 

 The
 `Mip Filter` 
 parameter has the same possible values, with the addition of the option to allow for the value of
 `None` 
 , which specifies that mipmapping isn’t used.
 

 Below is an example of a simple node graph that uses the Image 2Dnode to create a material from an image.
 

![](https://docs-assets.developer.apple.com/published/4b154925c4f38a518e9e33b9c2bebdb7/Image2dGraph.png)

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/faa74d1975d208dcd704a5c3692a3285/Image2dMaterial.png)

 A texture with RealityKit properties.

[See Also](/documentation/shadergraph/realitykit/image-2d-(realitykit)#see-also)
--------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/realitykit/image-2d-(realitykit)#nodes)

[`Geometry Modifier (Reality
  Kit)`](/documentation/shadergraph/realitykit/geometry-modifier-(realitykit))

 A function that manipulates the location of a model’s vertices, run once per vertex.
 

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
 

