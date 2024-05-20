# texture-coordinates


[Parameter Types](/documentation/shadergraph/geometric/texture-coordinates#Parameter-Types)
-------------------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

[Parameter description](/documentation/shadergraph/geometric/texture-coordinates#Parameter-description)
-------------------------------------------------------------------------------------------------------

`Index` 

 The index of the texture coordinates to be referenced. The default value is
 `0` 
 .
 

 The 2D or 3D texture coordinates of the currently-processed data.

[See Also](/documentation/shadergraph/geometric/texture-coordinates#see-also)
-----------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/texture-coordinates#nodes)

[`Position`](/documentation/shadergraph/geometric/position)

 The coordinates of the currently-processed data in a given coordinate space.
 

[`Normal`](/documentation/shadergraph/geometric/normal)

 The geometric normal of the currently-processed data in a given coordinate space.
 

[`Tangent`](/documentation/shadergraph/geometric/tangent)

 The geometric tangent of the currently-processed data in a given coordinate space.
 

[`Bitangent`](/documentation/shadergraph/geometric/bitangent)

 The geometric bitangent vector of the currently-processed data in a given coordinate space.
 

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
 

