# ramp-vertical


[Parameter Types](/documentation/shadergraph/2d-procedural/ramp-vertical#Parameter-Types)
-----------------------------------------------------------------------------------------

* [Ramp Vertical (float)](#)
* [Ramp Vertical (color3f)](#)
* [Ramp Vertical (vector3f)](#)
* [Ramp Vertical (vector4f)](#)
* [Ramp Vertical (color4f)](#)
* [Ramp Vertical (vector4h)](#)
* [Ramp Vertical (vector3h)](#)
* [Ramp Vertical (vector2f)](#)
* [Ramp Vertical (half)](#)
* [Ramp Vertical (vector2h)](#)

| Input | Type |
| --- | --- |
| `Top` | Float |
| `Bottom` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Top` | Color3 |
| `Bottom` | Color3 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Top` | Vector3f |
| `Bottom` | Vector3f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Top` | Vector4f |
| `Bottom` | Vector4f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `Top` | Color4 |
| `Bottom` | Color4 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Top` | Vector4h |
| `Bottom` | Vector4h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `Top` | Vector3h |
| `Bottom` | Vector3h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `Top` | Vector2f |
| `Bottom` | Vector2f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Top` | Half |
| `Bottom` | Half |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `Top` | Vector2h |
| `Bottom` | Vector2h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

[Parameter Descriptions](/documentation/shadergraph/2d-procedural/ramp-vertical#Parameter-Descriptions)
-------------------------------------------------------------------------------------------------------

`Top` 

 The top value of the interpolation.
 

`Bottom` 

 The bottom value of the interpolation.
 

`Texture coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

[Discussion](/documentation/shadergraph/2d-procedural/ramp-vertical#Discussion)
-------------------------------------------------------------------------------

 This node uses interpolation to create a vertical ramp or gradient from two values. Any point within the output ramp is a mix of the two values. A given point is more similar to the value that its vertical position is closer to. Below is a an example of a simple node graph that uses Ramp Vertical to create a color gradient.
 

![](https://docs-assets.developer.apple.com/published/fe4213c8fa2452496e89ae10982502ab/RampVerticalGraph.png)

 The image below shows the resulting texture, along with the color values on either side.
 

![](https://docs-assets.developer.apple.com/published/03252167c26d5947d2711bff9736ac34/RampVerticalMaterial.png)

 A top-to-bottom linear value ramp (gradient) generator.

[See Also](/documentation/shadergraph/2d-procedural/ramp-vertical#see-also)
---------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/ramp-vertical#nodes)

[`Ramp Horizontal`](/documentation/shadergraph/2d-procedural/ramp-horizontal)

 A left-to-right linear value ramp (gradient) generator.
 

[`Ramp 4 Corners`](/documentation/shadergraph/2d-procedural/ramp-4-corners)

 A four-point linear value ramp (gradient) generator.
 

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
 

