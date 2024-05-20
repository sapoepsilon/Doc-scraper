# convert


[Parameter Types](/documentation/shadergraph/data/convert#Parameter-Types)
--------------------------------------------------------------------------

* [Convert (float color3f)](#)
* [Convert (vector2f vector2h)](#)
* [Convert (vector2h vector2f)](#)
* [Convert (vector3h vector3f)](#)
* [Convert (half vector3f)](#)
* [Convert (vector4h vector4f)](#)
* [Convert (float vector4f)](#)
* [Convert (half vector4f)](#)
* [Convert (half integer)](#)
* [Convert (vector4f color4f)](#)
* [Convert (bool half)](#)
* [Convert (vector2f vector3f)](#)
* [Convert (half float)](#)
* [Convert (bool float)](#)
* [Convert (float integer)](#)
* [Convert (vector3f vector3h)](#)
* [Convert (float vector3f)](#)
* [Convert (vector4f vector3f)](#)
* [Convert (integer half)](#)
* [Convert (vector3f vector4f)](#)
* [Convert (color3f vector3f)](#)
* [Convert (color4f vector4f)](#)
* [Convert (integer float)](#)
* [Convert (half color4f)](#)
* [Convert (float half)](#)
* [Convert (vector3f vector2f)](#)
* [Convert (vector3h color3f)](#)
* [Convert (color3f color4f)](#)
* [Convert (vector4f vector4h)](#)
* [Convert (float color4f)](#)
* [Convert (half vector2f)](#)
* [Convert (half color3f)](#)
* [Convert (float vector2f)](#)
* [Convert (vector3f to color3f)](#)
* [Convert (color4f color3f)](#)

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

| Input | Type |
| --- | --- |
| `In` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

| Input | Type |
| --- | --- |
| `In` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

| Input | Type |
| --- | --- |
| `In` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

| Input | Type |
| --- | --- |
| `In` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

| Input | Type |
| --- | --- |
| `In` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Half |

| Input | Type |
| --- | --- |
| `In` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

| Input | Type |
| --- | --- |
| `In` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `In` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

[Discussion](/documentation/shadergraph/data/convert#Discussion)
----------------------------------------------------------------

 The Convert node takes data of one type and outputs it in another form. The supported type conversions are shown above with the various convert node types. The convert node handles data types in the following ways:
 

* When converting a float to a color or vector, the convert node copies the float to all channels of the color or vector.
* When converting a color3 to a color4, the convert node sets the output alpha to
 `1
 
 .0`
* When converting a color4 to a color3, the alpha channel is dropped.
* When converting a boolean or integer to a float, the output is either
 `1
 
 .0` 
 or
 `0
 
 .0` 
 .
* When converting a vector2 to vector3 or a vector3 to a vector4, an additional channel with a value of
 `1
 
 .0` 
 is appended to the input vector.
* When converting a vector4 to a vector3 or a vector3 to a vector2, the last channel is dropped.

 Converts a stream from one data type to another.

[See Also](/documentation/shadergraph/data/convert#see-also)
------------------------------------------------------------

### [Nodes](/documentation/shadergraph/data/convert#nodes)

[`Swizzle`](/documentation/shadergraph/data/swizzle)

 Performs an arbitrary permutation of the channels of the input stream, returning a new stream of the specified type.
 

[`Combine 2`](/documentation/shadergraph/data/combine-2)

 Combines the channels from two streams into two channels of a single output stream of a compatible type.
 

[`Combine 3`](/documentation/shadergraph/data/combine-3)

 Combines the channels from three streams into three channels of a single output stream of a compatible type.
 

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
 

