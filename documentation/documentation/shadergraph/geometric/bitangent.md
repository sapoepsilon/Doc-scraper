# bitangent


[Parameter Types](/documentation/shadergraph/geometric/bitangent#Parameter-Types)
---------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Space` | String |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/geometric/bitangent#Parameter-descriptions)
-----------------------------------------------------------------------------------------------

`Space` 

 The space in which the shader defines the bitangent vector. Defaults to
 `object` 
 .
 

`Index` 

 The index of the texture coordinates that the node computes the tangent against. Default is
 `0` 
 .
 

[Discussion](/documentation/shadergraph/geometric/bitangent#Discussion)
-----------------------------------------------------------------------

 Valid values for the
 `Space` 
 parameter include the following:
 

* `model` 
 : The local coordinate space before the shader applies any local deformations or global transforms to the geometry.
* `object` 
 : The local coordinate space after the shader applies local deformations but before it applies global transforms to the geometry.
* `world` 
 : The global coordinate space after the shader applies both local deformations and global transforms to the geometry.

 The geometric bitangent vector of the currently-processed data in a given coordinate space.

[See Also](/documentation/shadergraph/geometric/bitangent#see-also)
-------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/bitangent#nodes)

[`Position`](/documentation/shadergraph/geometric/position)

 The coordinates of the currently-processed data in a given coordinate space.
 

[`Normal`](/documentation/shadergraph/geometric/normal)

 The geometric normal of the currently-processed data in a given coordinate space.
 

[`Tangent`](/documentation/shadergraph/geometric/tangent)

 The geometric tangent of the currently-processed data in a given coordinate space.
 

[`Texture Coordinates`](/documentation/shadergraph/geometric/texture-coordinates)

 The 2D or 3D texture coordinates of the currently-processed data.
 

[`Geometry Color`](/documentation/shadergraph/geometric/geometry-color)

 The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
 

[`Geometric Property`](/documentation/shadergraph/geometric/geometric-property)

 The value of the specified geometric property (defined using ) of the currently-bound geometry.
 

[`Reflect (Reality
  Kit)`](/documentation/shadergraph/geometric/reflect-(realitykit))

 Reflects a vector about another vector.
 

[`Refract (Reality
  Kit)`](/documentation/shadergraph/geometric/refract-(realitykit))

 Refracts a vector using a given normal and index of refraction (eta).
 

