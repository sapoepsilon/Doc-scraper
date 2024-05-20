# combine-3


[Parameter Types](/documentation/shadergraph/data/combine-3#Parameter-Types)
----------------------------------------------------------------------------

* [Combine 3 (color3f)](#)
* [Combine 3 (vector3h)](#)
* [Combine 3 (matrix3x3f)](#)
* [Combine 3 (integer3)](#)
* [Combine 3 (vector3f)](#)

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |
| `In 3` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In 1` | Half |
| `In 2` | Half |
| `In 3` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `In 1` | Vector3f |
| `In 2` | Vector3f |
| `In 3` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Matrix3x3f |

| Input | Type |
| --- | --- |
| `In 1` | Int32 |
| `In 2` | Int32 |
| `In 3` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Integer3 |

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |
| `In 3` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

 Combines the channels from three streams into three channels of a single output stream of a compatible type.

[See Also](/documentation/shadergraph/data/combine-3#see-also)
--------------------------------------------------------------

### [Nodes](/documentation/shadergraph/data/combine-3#nodes)

[`Convert`](/documentation/shadergraph/data/convert)

 Converts a stream from one data type to another.
 

[`Swizzle`](/documentation/shadergraph/data/swizzle)

 Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
 

[`Combine 2`](/documentation/shadergraph/data/combine-2)

 Combines the channels from two streams into two channels of a single output stream of a compatible type.
 

[`Combine 4`](/documentation/shadergraph/data/combine-4)

 Combines the channels from four streams into four channels of a single output stream of a compatible type.
 

[`Extract`](/documentation/shadergraph/data/extract)

 Generates a float stream from one channel of a color​N o​r vector​N ​stream.
 

[`Separate 2`](/documentation/shadergraph/data/separate-2)

 Outputs each of the channels of a vector2 or integer2 as individual float or integer outputs.
 

[`Separate 3`](/documentation/shadergraph/data/separate-3)

 Outputs each of the channels of a color3, vector3, or integer3 as individual float or integer outputs.
 

[`Separate 4`](/documentation/shadergraph/data/separate-4)

 Outputs each of the channels of a color4, vector4, or integer4 as individual float or integer outputs.
 

[`Primvar Reader (integer)`](/documentation/shadergraph/data/primvar-reader-(integer))

 A node that provides the ability for shading networks to consume integer data defined on geometry.
 

[`Primvar Reader (bool)`](/documentation/shadergraph/data/primvar-reader-(bool))

 A node that provides the ability for shading networks to consume boolean data defined on geometry.
 

[`Primvar Reader (float)`](/documentation/shadergraph/data/primvar-reader-(float))

 A node that provides the ability for shading networks to consume float data defined on geometry.
 

[`Primvar Reader (vector2f)`](/documentation/shadergraph/data/primvar-reader-(vector2f))

 A node that provides the ability for shading networks to consume float2 data defined on geometry.
 

[`Primvar Reader (vector3f)`](/documentation/shadergraph/data/primvar-reader-(vector3f))

 A node that provides the ability for shading networks to consume float3 data defined on geometry.
 

[`Primvar Reader (vector4f)`](/documentation/shadergraph/data/primvar-reader-(vector4f))

 A node that provides the ability for shading networks to consume float4 data defined on geometry.
 
