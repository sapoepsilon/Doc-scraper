# geometry-color


[Parameter Types](/documentation/shadergraph/geometric/geometry-color#Parameter-Types)
--------------------------------------------------------------------------------------

* [Geometry Color (float)](#)
* [Geometry Color (color3f)](#)
* [Geometry Color (color4f)](#)

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Float |

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

| Input | Type |
| --- | --- |
| `Index` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

[Parameter description](/documentation/shadergraph/geometric/geometry-color#Parameter-description)
--------------------------------------------------------------------------------------------------

`Index` 

 The index of the color the node references. The default value is
 `0` 
 .
 

 The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.

[See Also](/documentation/shadergraph/geometric/geometry-color#see-also)
------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/geometry-color#nodes)

[`Position`](/documentation/shadergraph/geometric/position)

 The coordinates of the currently-processed data in a given coordinate space.
 

[`Normal`](/documentation/shadergraph/geometric/normal)

 The geometric normal of the currently-processed data in a given coordinate space.
 

[`Tangent`](/documentation/shadergraph/geometric/tangent)

 The geometric tangent of the currently-processed data in a given coordinate space.
 

[`Bitangent`](/documentation/shadergraph/geometric/bitangent)

 The geometric bitangent vector of the currently-processed data in a given coordinate space.
 

[`Texture Coordinates`](/documentation/shadergraph/geometric/texture-coordinates)

 The 2D or 3D texture coordinates of the currently-processed data.
 

[`Geometric Property`](/documentation/shadergraph/geometric/geometric-property)

 The value of the specified geometric property (defined using ) of the currently-bound geometry.
 

[`Reflect (Reality
  Kit)`](/documentation/shadergraph/geometric/reflect-(realitykit))

 Reflects a vector about another vector.
 

[`Refract (Reality
  Kit)`](/documentation/shadergraph/geometric/refract-(realitykit))

 Refracts a vector using a given normal and index of refraction (eta).
 

