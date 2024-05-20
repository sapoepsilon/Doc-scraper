# worley-noise-3d


[Parameter Types](/documentation/shadergraph/3d-procedural/worley-noise-3d#Parameter-Types)
-------------------------------------------------------------------------------------------

* [Worley Noise 3D (float)](#)
* [Worley Noise 3D (vector2f)](#)
* [Worley Noise 3D (vector3f)](#)

| Input | Type |
| --- | --- |
| `Position` | Vector3f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Position` | Vector3f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Position` | Vector3f |
| `Jitter` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/3d-procedural/worley-noise-3d#Parameter-descriptions)
---------------------------------------------------------------------------------------------------------

`Position` 

 The 3D coordinates at which the node reads the data in order to map the texture onto a surface. The default uses the current 3D object-space coordinates.
 

`Jitter` 

 The amount of
 *jitter* 
 or shift the center of each cell experiences. The default value is
 `1
 
 .0` 
 . A smaller value creates a more regular pattern, and
 `0` 
 creates perfect squares.
 

[Discussion](/documentation/shadergraph/3d-procedural/worley-noise-3d#Discussion)
---------------------------------------------------------------------------------

 The Worley Noise 3D node procedurally generates nonuniform cellular regions. The node creates a finite number of center points, and each region is a polygon that surrounds the points closest to each center point. Because this node generates noise in 3D, the texture doesn’t repeat in the Z direction but rather continues as depth changes. Below is an example of a simple node graph that uses the Worley Noise 3D node to generate a black and white pattern procedurally.
 

![](https://docs-assets.developer.apple.com/published/93e069365411ee3b9980bbaac0872c99/WorleyNoise3dGraph.png)

 Multiply the incoming texture coordinates with a constant float, which changes the frequency of the generated noise. A higher value corresponds to the pattern repeating more often. Then run the output through a convert node to change it to a black and white color value.
   

 Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/bdf0fcb2dbd86638217094fcc5ebedc6/WorleyNoise3dMaterial.png)

 A 3D Worley noise generator.

[See Also](/documentation/shadergraph/3d-procedural/worley-noise-3d#see-also)
-----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/3d-procedural/worley-noise-3d#nodes)

[`Noise 3D`](/documentation/shadergraph/3d-procedural/noise-3d)

 A 3D Perlin noise generator.
 

[`Fractal Noise 3D`](/documentation/shadergraph/3d-procedural/fractal-noise-3d)

 Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.
 

[`Cellular Noise 3D`](/documentation/shadergraph/3d-procedural/cellular-noise-3d)

 A 3D cellular noise generator.
 

