# noise-2d


[Parameter Types](/documentation/shadergraph/2d-procedural/noise-2d#Parameter-Types)
------------------------------------------------------------------------------------

* [Noise 2D (float)](#)
* [Noise 2D (color3f FA)](#)
* [Noise 2D (vector4f)](#)
* [Noise 2D (color4f FA)](#)
* [Noise 2D (vector3f FA)](#)
* [Noise 2D (vector2f)](#)
* [Noise 2D (vector2f FA)](#)
* [Noise 2D (color3f)](#)
* [Noise 2D (color4f)](#)
* [Noise 2D (vector3f)](#)
* [Noise 2D (vector4f FA)](#)

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector2f |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Pivot` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

[Parameter descriptions](/documentation/shadergraph/2d-procedural/noise-2d#Parameter-descriptions)
--------------------------------------------------------------------------------------------------

`Amplitude` 

 The intensity of the generated noise. The higher the amplitude, the more pronounced the variations of the noise pattern.
 

`Pivot` 

 The neutral value of the noise. This value is the noise’s minimum value, and is added to the output after the output is multiplied by the amplitude.
 

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

[Discussion](/documentation/shadergraph/2d-procedural/noise-2d#Discussion)
--------------------------------------------------------------------------

 The Noise 2D shader node procedurally generates Perlin noise patterns that you can use to add texture and variation to materials. All noise values that are procedurally generated are numbers between
 `0` 
 and
 `1` 
 before the amplitude and pivot are applied. Below is an example of a simple node graph that uses the Noise 2D Node to generate a black and white pattern procedurally.
 

![](https://docs-assets.developer.apple.com/published/1b5a1202e65fb150252ddc171f1dc53a/Noise2dGraph.png)

 Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/0731a19532c2cf80f4640eb844465f64/Noise2dMaterial.png)

 A 2D Perlin noise generator.

[See Also](/documentation/shadergraph/2d-procedural/noise-2d#see-also)
----------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/noise-2d#nodes)

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
 

[`Cellular Noise 2D`](/documentation/shadergraph/2d-procedural/cellular-noise-2d)

 A 2D cellular noise generator.
 

[`Worley Noise 2D`](/documentation/shadergraph/2d-procedural/worley-noise-2d)

 A 2D Worley noise generator.
 

