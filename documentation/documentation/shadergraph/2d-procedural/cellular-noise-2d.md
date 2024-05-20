# cellular-noise-2d


[Parameter Types](/documentation/shadergraph/2d-procedural/cellular-noise-2d#Parameter-Types)
---------------------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

[Parameter descriptions](/documentation/shadergraph/2d-procedural/cellular-noise-2d#Parameter-descriptions)
-----------------------------------------------------------------------------------------------------------

`Texture Coordinates` 

 The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current
 *UV* 
 coordinates, in which
 *U* 
 is the horizontal axis and
 *V* 
 is the vertical axis.
 

[Discussion](/documentation/shadergraph/2d-procedural/cellular-noise-2d#Discussion)
-----------------------------------------------------------------------------------

 The Cellular Noise 2D shader node procedurally generates noise patterns that can be used to add texture and variation to materials. Below is an example of a simple node graph that uses the Cellular Noise 2D Node to generate a black and white pattern procedurally.
 

![](https://docs-assets.developer.apple.com/published/e7cba5b397d0b79f7db7a9a072b3e93d/CellNoise2dGraph.png)

 Multiply the incoming texture coordinates with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. The output of the node runs through a convert node in order to change the float output to a black and white color output. Below, the resulting texture applies to a cube.
 

![](https://docs-assets.developer.apple.com/published/c346f62f96cb87deeccd42e14b529293/CellNoise2dMaterial.png)

 A 2D cellular noise generator.

[See Also](/documentation/shadergraph/2d-procedural/cellular-noise-2d#see-also)
-------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/2d-procedural/cellular-noise-2d#nodes)

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
 

[`Worley Noise 2D`](/documentation/shadergraph/2d-procedural/worley-noise-2d)

 A 2D Worley noise generator.
 

