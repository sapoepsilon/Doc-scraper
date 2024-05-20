# time-float


[Parameter Types](/documentation/shadergraph/application/time-(float)#Parameter-Types)
--------------------------------------------------------------------------------------

| Output | Type |
| --- | --- |
| `Out` | Float |

[Discussion](/documentation/shadergraph/application/time-(float)#Discussion)
----------------------------------------------------------------------------

 The Time node outputs a float representing the current time in seconds. When applied or connected to other nodes, this value changes constantly, allowing for dynamic materials. Below is an example of a simple node graph that causes an image texture to scroll in real time.
 

![](https://docs-assets.developer.apple.com/published/cff64c2ca64dd8e94442e51f2b648d9f/TimeGraph.png)

 Adding Time to the incoming texture coordinates horizontal component causes the texture to “scroll” along the horizontal plane. Below, the resulting texture applies to a cube.
 

[Play](#)

 The current time in seconds.

[See Also](/documentation/shadergraph/application/time-(float)#see-also)
------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/application/time-(float)#nodes)

[`Up Direction`](/documentation/shadergraph/application/up-direction)

 The direction of the up vector.
 

