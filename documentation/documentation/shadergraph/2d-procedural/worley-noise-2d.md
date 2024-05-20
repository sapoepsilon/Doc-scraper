# worley-noise-2d


[Parameter Types](/documentation/shadergraph/2d-procedural/worley-noise-2d#Parameter-Types)
-------------------------------------------------------------------------------------------

* [Worley Noise 2D (float)](#)
* [Worley Noise 2D (vector2f)](#)
* [Worley Noise 2D (vector3f)](#)

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter description](/documentation/shadergraph/2d-procedural/worley-noise-2d#Parameter-description)
-------------------------------------------------------------------------------------------------------

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default uses the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

`Jitter` 

 The amount to
 *jitter* 
 or shift the center of each cell experiences. The default value is
 `1
 
 .0` 
 . A smaller value creates a more regular pattern, and
 `0` 
 creates perfect squares.
 

[Discussion](/documentation/shadergraph/2d-procedural/worley-noise-2d#Discussion)
---------------------------------------------------------------------------------

 The Worley Noise 2D node procedurally generates nonuniform cellular regions. A finite number of center points are created, and each region is a polygon that surrounds the points closest to each center point. Below is an example of a simple node graph that uses the Worley Noise 2D Node to generate a black and white pattern procedurally.
 

![](https://docs-assets.developer.apple.com/published/62d4fabeb371ea9ca3f41c9279d37cb8/WorleyNoise2dGraph.png)

 Multiply the incoming texture coordinates with a constant float, which changes the frequency of the generated noise. A higher value coresponds to the pattern repeating more often. You then run the output through a convert node to change it to a black and white color value.
   

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/0e472112c39c6c41e216af35b03029b5/WorleyNoise2dMaterial.png)

 A 2D Worley noise generator.

[See Also](/documentation/shadergraph/2d-procedural/worley-noise-2d#see-also)
-----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/worley-noise-2d#nodes)

[`Ramp Horizontal`](/documentation/shadergraph/2d-procedural/ramp-horizontal)

 A left-to-right linear value ramp (gradient) generator.
 

[`Ramp Vertical`](/documentation/shadergraph/2d-procedural/ramp-vertical)

 A top-to-bottom linear value ramp (gradient) generator.
 

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
 

