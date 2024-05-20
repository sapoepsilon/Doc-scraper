# refract-realitykit


[Parameter Types](/documentation/shadergraph/geometric/refract-(realitykit)#Parameter-Types)
--------------------------------------------------------------------------------------------

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Normal` | Vector3f |
| `Eta` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

[Parameter descriptions](/documentation/shadergraph/geometric/refract-(realitykit)#Parameter-descriptions)
----------------------------------------------------------------------------------------------------------

`In` 

 The vector to refract.
 

`Normal` 

 The normal of the surface from which the
 `In` 
 vector refracts.
 

`Eta` 

 The index of refraction.
 

[Discussion](/documentation/shadergraph/geometric/refract-(realitykit)#Discussion)
----------------------------------------------------------------------------------

 The Refract node takes an incident vector
 `In` 
 and calculates the direction of refraction off a surface.
 

 Note
 

 The vectors passed as the
 `In` 
 and
 `Normal` 
 parameters must both already be normalized in order to get the desired output.
 

 Refracts a vector using a given normal and index of refraction (eta).

[See Also](/documentation/shadergraph/geometric/refract-(realitykit)#see-also)
------------------------------------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric/refract-(realitykit)#nodes)

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
 

[`Reflect (Reality
  Kit)`](/documentation/shadergraph/geometric/reflect-(realitykit))

 Reflects a vector about another vector.
 

