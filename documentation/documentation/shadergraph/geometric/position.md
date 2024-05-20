# position


[Parameter Types](/documentation/shadergraph/geometric/position#Parameter-Types)
--------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `Space` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter description](/documentation/shadergraph/geometric/position#Parameter-description)
--------------------------------------------------------------------------------------------

`Space` 

 The space in which the shader defines the position vector. The valid spaces for this input are
 `model` 
 ,
 `object` 
 ,
 `tangent` 
 , and
 `world` 
 . The default value is
 `object` 
 .
 

 The coordinates of the currently-processed data in a given coordinate space.

[See Also](/documentation/shadergraph/geometric/position#see-also)
------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/position#nodes)

[`Normal`](/documentation/shadergraph/geometric/normal)

 The geometric normal of the currently-processed data in a given coordinate space.
 

[`Tangent`](/documentation/shadergraph/geometric/tangent)

 The geometric tangent of the currently-processed data in a given coordinate space.
 

[`Bitangent`](/documentation/shadergraph/geometric/bitangent)

 The geometric bitangent vector of the currently-processed data in a given coordinate space.
 

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
 

