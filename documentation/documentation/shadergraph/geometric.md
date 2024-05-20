# geometric


[Overview](/documentation/shadergraph/geometric#overview)
---------------------------------------------------------

 When the GPU applies your graph to a scene, geometric nodes reflect the data value the system is currently processing. Use these nodes to get details about that data value, such as its coordinates, normal, or tangent information. Alternatively, use the Reflect and Refract nodes to modify vectors relative to the current data value.
 

 Access scene geometry while your graph runs.

[Topics](/documentation/shadergraph/geometric#topics)
-----------------------------------------------------

### [Nodes](/documentation/shadergraph/geometric#nodes)

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
 

[`Reflect (Reality Kit)`](/documentation/shadergraph/geometric/reflect-(realitykit))

 Reflects a vector about another vector.
 

[`Refract (Reality Kit)`](/documentation/shadergraph/geometric/refract-(realitykit))

 Refracts a vector using a given normal and index of refraction (eta).
 

