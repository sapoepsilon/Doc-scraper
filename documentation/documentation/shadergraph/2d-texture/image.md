# image


[Parameter Types](/documentation/shadergraph/2d-texture/image#Parameter-Types)
------------------------------------------------------------------------------

* [Image (float)](#)
* [Image (half)](#)
* [Image (vector4f)](#)
* [Image (vector3f)](#)
* [Image (color3f)](#)
* [Image (color4f)](#)
* [Image (vector2f)](#)

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Float |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Half |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector4f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector3f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Color3 |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Color4 |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector2f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

[Parameter descriptions](/documentation/shadergraph/2d-texture/image#Parameter-descriptions)
--------------------------------------------------------------------------------------------

`File` 

 The image file to use for the texture.
 

`Default` 

 The default value to use if the ​file​ reference fails to resolve.
 

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

`Uaddressmode` 

 The way that the node will handle
 *U* 
 values outside of the range of
 `0-1` 
 .
 

`Vaddressmode` 

 The way that the node will handle
 *V* 
 values outside of the range of
 `0-1` 
 .
 

`Filter Type` 

 The type of texture filtering the node will use.
 

[Discussion](/documentation/shadergraph/2d-texture/image#Discussion)
--------------------------------------------------------------------

 The Image node creates a material from an image file. This node samples data from a single image, and maps it onto an object. The address modes for the Image node tell it how to handle
 *U* 
 and
 *V* 
 values outside of the normal range of
 `0-1` 
 .
 `Uaddressmode` 
 and
 `Vaddressmode` 
 take one of four values to determine their behavior.
 

* constant: Texture coordinates outside the normal range return the
 `Default` 
 input.
* clamp: Texture coordinates outside the normal range are clamped to the normal range. Any values greater than
 `1` 
 will be set to
 `1` 
 , and any values less than
 `0` 
 will be set to
 `0`
* periodic: Texture coordinates outside the normal range will “wrap around.” This behavior is effectively equivalent to applying modulo 1 to the coordinates.
* mirror: Texture coordinates outside the normal range will be mirrored.

![](https://docs-assets.developer.apple.com/published/a5c21ae2f55ee54ef910b7d0f2941c4f/ImageAddressMode1.png)

 Constant
 

![](https://docs-assets.developer.apple.com/published/3b2d0556868d5496815f8c86cb7f4a8d/ImageAddressMode2.png)

 Clamp
 

![](https://docs-assets.developer.apple.com/published/b31f98bbcd0a9cdbf393da99d549082a/ImageAddressMode3.png)

 Mirror
 

![](https://docs-assets.developer.apple.com/published/675900c021a8416e3336941e357076ef/ImageAddressMode4.png)

 Periodic
 

 Below is an example of a simple node graph that uses the Image node to create a material from an image.
 

![](https://docs-assets.developer.apple.com/published/98d58918f59501fe37fa0e93fa270b92/ImageGraph.png)

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/353f7f54898ac6f9c13f9374acc8cb66/ImageMaterial.png)

 A texture referencing a 2D image file.

[See Also](/documentation/shadergraph/2d-texture/image#see-also)
----------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-texture/image#nodes)

[`Tiled Image`](/documentation/shadergraph/2d-texture/tiled-image)

 Samples data from an image with provisions for offsetting and tiling in UV space.
 

[`UV Texture`](/documentation/shadergraph/2d-texture/uv-texture)

 A MaterialX version of USD UV Texture reader.
 

[`Transform 2D`](/documentation/shadergraph/2d-texture/transform-2d)

 A node that applies an affine transformation to a 2d input.
 

