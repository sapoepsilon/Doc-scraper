# ramp-4-corners


[Parameter Types](/documentation/shadergraph/2d-procedural/ramp-4-corners#Parameter-Types)
------------------------------------------------------------------------------------------

* [Ramp 4 Corners (float)](#)
* [Ramp 4 Corners (vector3f)](#)
* [Ramp 4 Corners (color3f)](#)
* [Ramp 4 Corners (color4f)](#)
* [Ramp 4 Corners (vector2f)](#)
* [Ramp 4 Corners (vector4f)](#)

| Input | Type |
| --- | --- |
| `Top Left` | Float |
| `Top Right` | Float |
| `Bottom Left` | Float |
| `Bottom Right` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Top Left` | Vector3f |
| `Top Right` | Vector3f |
| `Bottom Left` | Vector3f |
| `Bottom Right` | Vector3f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Top Left` | Color3 |
| `Top Right` | Color3 |
| `Bottom Left` | Color3 |
| `Bottom Right` | Color3 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Top Left` | Color4 |
| `Top Right` | Color4 |
| `Bottom Left` | Color4 |
| `Bottom Right` | Color4 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Top Left` | Vector2f |
| `Top Right` | Vector2f |
| `Bottom Left` | Vector2f |
| `Bottom Right` | Vector2f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Top Left` | Vector4f |
| `Top Right` | Vector4f |
| `Bottom Left` | Vector4f |
| `Bottom Right` | Vector4f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

[Parameter descriptions](/documentation/shadergraph/2d-procedural/ramp-4-corners#Parameter-descriptions)
--------------------------------------------------------------------------------------------------------

`Top left` 

 The top-left value of the four-point interpolation.
 

`Top right` 

 The top-right value of the four-point interpolation.
 

`Bottom left` 

 The bottom-left value of the four-point interpolation.
 

`Bottom right` 

 The bottom-right value of the four-point interpolation.
 

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

[Discussion](/documentation/shadergraph/2d-procedural/ramp-4-corners#Discussion)
--------------------------------------------------------------------------------

 This node uses bilinear interpolation to create a ramp from four corner values. Any point within the output ramp is a mix of one of the four corner values. A given point is more similar to a corner value the closer its position is to that corner. Below is a an example of a simple node graph that uses Ramp 4 Corners to create a gradient with four different colors.
 

![](https://docs-assets.developer.apple.com/published/1778842288c4d7928f63c92b5eb32703/Ramp4Graph.png)

 The image below shows the resulting texture along with the color values on each corner.
 

![](https://docs-assets.developer.apple.com/published/1d6fc6df1e54b2e218c0941bff4530e0/Ramp4Material.png)

 A four-point linear value ramp (gradient) generator.

[See Also](/documentation/shadergraph/2d-procedural/ramp-4-corners#see-also)
----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/ramp-4-corners#nodes)

[`Ramp Horizontal`](/documentation/shadergraph/2d-procedural/ramp-horizontal)

 A left-to-right linear value ramp (gradient) generator.
 

[`Ramp Vertical`](/documentation/shadergraph/2d-procedural/ramp-vertical)

 A top-to-bottom linear value ramp (gradient) generator.
 

[`Split Horizontal`](/documentation/shadergraph/2d-procedural/split-horizontal)

 A left-to-right split matte, split at a specified U value.
 

[`Split Vertical`](/documentation/shadergraph/2d-procedural/split-vertical)

 A top-to-bottom split matte, split at a specified V value.
 

[`Noise 2D`](/documentation/shadergraph/2d-procedural/noise-2d)

 A 2D Perlin noise generator.
 

[`Cellular Noise 2D`](/documentation/shadergraph/2d-procedural/cellular-noise-2d)

 A 2D cellular noise generator.
 

[`Worley Noise 2D`](/documentation/shadergraph/2d-procedural/worley-noise-2d)

 A 2D Worley noise generator.
 

