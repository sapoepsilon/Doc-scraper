# fractal-noise-3d


[Parameter Types](/documentation/shadergraph/3d-procedural/fractal-noise-3d#Parameter-Types)
--------------------------------------------------------------------------------------------

* [Fractal Noise 3D (float)](#)
* [Fractal Noise 3D (vector2f FA)](#)
* [Fractal Noise 3D (vector3f FA)](#)
* [Fractal Noise 3D (color4f FA)](#)
* [Fractal Noise 3D (vector2f)](#)
* [Fractal Noise 3D (color3f)](#)
* [Fractal Noise 3D (color3f FA)](#)
* [Fractal Noise 3D (color4f)](#)
* [Fractal Noise 3D (vector4f)](#)
* [Fractal Noise 3D (vector3f)](#)
* [Fractal Noise 3D (vector4f FA)](#)

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector2f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

[Parameter descriptions](/documentation/shadergraph/3d-procedural/fractal-noise-3d#Parameter-descriptions)
----------------------------------------------------------------------------------------------------------

`Amplitude` 

 The intensity of the generated noise. The higher the amplitude, the more pronounced the variations of the noise pattern.
 

`Octaves` 

 The number of layers of 3D Perlin noise that the node sums together. The default value is 3.
 

`Lacunarity` 

 The exponential scale between each octave. This value determines how different each successive octave or layer of Perlin noise is from one another. The default value is
 `2
 
 .0` 

`Diminish` 

 The rate that the amplitude of each successive octave is decreased. Maintain the value for this parameter in the range of
 `0
 
 .0-1
 
 .0` 
 . The default value is
 `0
 
 .5` 
 .
 

`Position` 

 The 3D coordinates at which the data is read in order to map the texture onto a surface. The default is to use the current 3D object-space coordinates.
 

[Discussion](/documentation/shadergraph/3d-procedural/fractal-noise-3d#Discussion)
----------------------------------------------------------------------------------

 The Fractal Noise node produces its output by summing up multiple layers or octaves of 3D Perlin noise. The more octaves in the fractal noise, the finer the detail of the noise. Each successive octave differs from the previous; the
 `Lacunarity` 
 and
 `Diminish` 
 parameters determine the difference.
 *Lacunarity* 
 refers to the difference in frequency between each octavex. As this value increases, the resulting fractal noise becomes more uneven and less smooth.
 *Diminish* 
 refers to how the amplitude changes between octaves. A value of
 `1` 
 indicates no change to the amplitude. As the value decreases, the amplitude from octave to octave decreases more quickly. Below is an example of a simple node graph that uses the Fractal Noise 3D node to generate a black and white pattern procedurally.
 

![](https://docs-assets.developer.apple.com/published/1623056b5ba6202fb824330ce949c39e/FractalNoise3DGraph.png)

 Multiply the incoming position with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. Below, the resulting texture applies to a cube with various values for each parameter. All values are the default, unless specified under the image.
 

![](https://docs-assets.developer.apple.com/published/c23b310eb88ce7fe0b2f7e7c4fe88036/Fractal3DOctaves1.png)

 1 Octave
 

![](https://docs-assets.developer.apple.com/published/1559ce00401ed2d1827a945699610fe1/Fractal3DOctaves3.png)

 3 Octaves
 

![](https://docs-assets.developer.apple.com/published/571202d34b43b741a3bfc8b63d1f5839/Fractal3DOctaves5.png)

 5 Octaves
 

![](https://docs-assets.developer.apple.com/published/e72e9e2ded38148ba59b0c96d630f322/Fractal3DLacunarity1.png)

 Lacunarity of 1
 

![](https://docs-assets.developer.apple.com/published/1559ce00401ed2d1827a945699610fe1/Fractal3DLacunarity2.png)

 Lacunarity of 2
 

![](https://docs-assets.developer.apple.com/published/30cc09fe6e18c0c843c0e1541c07eb3e/Fractal3DLacunarity5.png)

 Lacunarity of 5
 

![](https://docs-assets.developer.apple.com/published/0efe5fc6e911cb096b733362fb2c6927/Fractal3DDiminish0.2.png)

 Diminish of 0.2
 

![](https://docs-assets.developer.apple.com/published/1559ce00401ed2d1827a945699610fe1/Fractal3DDiminish0.5.png)

 Diminish of 0.5
 

![](https://docs-assets.developer.apple.com/published/284a8e2b82918359c95c1d78e6876247/Fractal3DDiminish1.png)

 Diminish of 1
 

 Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.

[See Also](/documentation/shadergraph/3d-procedural/fractal-noise-3d#see-also)
------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/3d-procedural/fractal-noise-3d#nodes)

[`Noise 3D`](/documentation/shadergraph/3d-procedural/noise-3d)

 A 3D Perlin noise generator.
 

[`Cellular Noise 3D`](/documentation/shadergraph/3d-procedural/cellular-noise-3d)

 A 3D cellular noise generator.
 

[`Worley Noise 3D`](/documentation/shadergraph/3d-procedural/worley-noise-3d)

 A 3D Worley noise generator.
 

