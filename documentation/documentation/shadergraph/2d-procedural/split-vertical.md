# split-vertical


[Parameter Types](/documentation/shadergraph/2d-procedural/split-vertical#Parameter-Types)
------------------------------------------------------------------------------------------

* [Split Vertical (float)](#)
* [Split Vertical (vector3f)](#)
* [Split Vertical (vector2f)](#)
* [Split Vertical (color3f)](#)
* [Split Vertical (vector2h)](#)
* [Split Vertical (vector3h)](#)
* [Split Vertical (vector4h)](#)
* [Split Vertical (color4f)](#)
* [Split Vertical (vector4f)](#)
* [Split Vertical (half)](#)

| Input | Type |
| --- | --- |
| `Top` | Float |
| `Bottom` | Float |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Top` | Vector3f |
| `Bottom` | Vector3f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Top` | Vector2f |
| `Bottom` | Vector2f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Top` | Color3 |
| `Bottom` | Color3 |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Top` | Vector2h |
| `Bottom` | Vector2h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `Top` | Vector3h |
| `Bottom` | Vector3h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `Top` | Vector4h |
| `Bottom` | Vector4h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `Top` | Color4 |
| `Bottom` | Color4 |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Top` | Vector4f |
| `Bottom` | Vector4f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `Top` | Half |
| `Bottom` | Half |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

[Parameter description](/documentation/shadergraph/2d-procedural/split-vertical#Parameter-description)
------------------------------------------------------------------------------------------------------

`Top` 

 The value of the left side of the split.
 

`Bottom` 

 The value of the right side of the split.
 

`Center` 

 The
 *V* 
 value at which the output is split. Everything above this value will be equal to the
 `Top` 
 input; everything below this value will be equal to the
 `Bottom` 
 input. This parameter ranges between
 `0` 
 and
 `1` 
 .
 

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default uses the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

[Discussion](/documentation/shadergraph/2d-procedural/split-vertical#Discussion)
--------------------------------------------------------------------------------

 This node creates two distinct regions along the vertical axis. The value of the
 `Center` 
 input determines the regions. A value of
 `0` 
 establishes the center at the top-most, position causing the output to always be equal to the
 `Top` 
 input. A value of
 `1` 
 establishes the center at the bottom-most position. Below is a an example of a simple node graph that uses Split Vertical to create a split color.
 

![](https://docs-assets.developer.apple.com/published/4c238efca001e7e1d912c0d1b322cfd9/SplitVerticalGraph.png)

 By editing the center value, the texture can be changed to show a larger top or bottom region. The image below shows the resulting textures.
 

![](https://docs-assets.developer.apple.com/published/e93fc156dba3409fa1a0c50ceaeda4f9/SplitVerticalMaterial1.png)

![](https://docs-assets.developer.apple.com/published/eb2b01bf5242b137759ce179b7770b48/SplitVerticalMaterial2.png)

![](https://docs-assets.developer.apple.com/published/85cd9f6ac19824561fa752a94d234455/SplitVerticalMaterial3.png)

 A top-to-bottom split matte, split at a specified V value.

[See Also](/documentation/shadergraph/2d-procedural/split-vertical#see-also)
----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/split-vertical#nodes)

[`Ramp Horizontal`](/documentation/shadergraph/2d-procedural/ramp-horizontal)

 A left-to-right linear value ramp (gradient) generator.
 

[`Ramp Vertical`](/documentation/shadergraph/2d-procedural/ramp-vertical)

 A top-to-bottom linear value ramp (gradient) generator.
 

[`Ramp 4 Corners`](/documentation/shadergraph/2d-procedural/ramp-4-corners)

 A four-point linear value ramp (gradient) generator.
 

[`Split Horizontal`](/documentation/shadergraph/2d-procedural/split-horizontal)

 A left-to-right split matte, split at a specified U value.
 

[`Noise 2D`](/documentation/shadergraph/2d-procedural/noise-2d)

 A 2D Perlin noise generator.
 

[`Cellular Noise 2D`](/documentation/shadergraph/2d-procedural/cellular-noise-2d)

 A 2D cellular noise generator.
 

[`Worley Noise 2D`](/documentation/shadergraph/2d-procedural/worley-noise-2d)

 A 2D Worley noise generator.
 

