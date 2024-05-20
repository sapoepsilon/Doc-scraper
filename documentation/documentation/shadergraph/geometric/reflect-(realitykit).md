# reflect-realitykit


[Parameter Types](/documentation/shadergraph/geometric/reflect-(realitykit)#Parameter-Types)
--------------------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Normal` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/geometric/reflect-(realitykit)#Parameter-descriptions)
----------------------------------------------------------------------------------------------------------

`In` 

 The input vector to be reflected.
 

`Normal` 

 The vector that the
 `In` 
 vector will be reflected with reference to.
 

[Discussion](/documentation/shadergraph/geometric/reflect-(realitykit)#Discussion)
----------------------------------------------------------------------------------

 The Reflect node reflects the
 `In` 
 vector by taking into account the surface orientation determined by the
 `Normal` 
 vector. The Reflect node first normalizes the
 `Normal` 
 vector and then calculates the reflection direction using the formula
 `In - 2 * dot(Normal, In) * Normal` 
 . In this equation,
 `dot()` 
 represents the dot product of the two vectors.
 

 Reflects a vector about another vector.

[See Also](/documentation/shadergraph/geometric/reflect-(realitykit)#see-also)
------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/reflect-(realitykit)#nodes)

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
 

[`Geometry Color`](/documentation/shadergraph/geometric/geometry-color)

 The color associated with the geometry at the currently-processed geometric position, typically defined by vertex color.
 

[`Geometric Property`](/documentation/shadergraph/geometric/geometric-property)

 The value of the specified geometric property (defined using ) of the currently-bound geometry.
 

[`Refract (Reality
  Kit)`](/documentation/shadergraph/geometric/refract-(realitykit))

 Refracts a vector using a given normal and index of refraction (eta).
 

