# compositing


Overview
--------

 The compositing process takes multiple input values and combines them in varying proportions to create a single output. You can use Compositing nodes to combine textures and achieve a specific appearance. For example, you might show a background texture only in places where the foreground texture is transparent. Compositing nodes support the combination of colors, but also other data types, such as vectors and floating-point numbers.
 

 Generate a single output from the combination of multiple data values.

Topics
------

### Nodes

 Premultiply
 

 Multiplies the RGB channels of the input by the alpha channel.
 

 Unpremultiply
 

 Divides the RGB channels of the input by the alpha channel.
 

 Additive Mix
 

 Adds foreground and background values.
 

 Subtractive Mix
 

 Subtracts foreground from background values.
 

 Difference
 

 Outputs the distance between foreground and background values.
 

 Burn
 

 A blend operation that darkens the foreground layer using the background.
 

 Dodge
 

 A blend operation that lightens the background layer depending on the foreground.
 

 Screen
 

 A blend operation that lightens areas that are darker than white.
 

 Overlay
 

 A blend operation that multiplies dark areas and screens light areas.
 

 Disjoint Over
 

 A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.
 

 In
 

 Outputs areas of foreground that overlap with the alpha of background.
 

 Mask
 

 Outputs areas of background that overlap with the alpha of foreground.
 

 Matte
 

 A merge operation that layers premultiplied foreground over background.
 

 Out
 

 Outputs areas of foreground that do not overlap with background.
 

 Over
 

 A merge operation that layers foreground over background, using the alpha of the foreground.
 

 Inside
 

 Multiplies a mask to all channels of the input.
 

 Outside
 

 Multiplies (1 - mask) to all channels of the input.
 

 Mix
 

 Mixes foreground and background inputs, weighting based on mix value.
 

