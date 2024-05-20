# nodegraph


[Discussion](/documentation/shadergraph/material/nodegraph#Discussion)
----------------------------------------------------------------------

 The NodeGraph node holds other node graphs that can be used in other materials. Use this node to define subgraphs that you commonly use and repeat. The NodeGraph node is a custom node that can be used in all of your other materials.
 

 The graphs in each NodeGraph node function almost exactly the same as the node graph for a custom material, and both use the same set of supported nodes. The main difference is that in a node graph, you can define any number of custom inputs or outputs. Name and define the type for each custom input and output.
 

 Note
 

 The names of any inputs or outputs can’t have spaces in them.
 

 Below is an example of a subgraph defined by a NodeGraph node and an example of using the NodeGraph node in a material. The subgraph takes inputs for horizontal and vertical speeds and outputs texture coordinates that cause an image to scroll either vertically, horizontally, or both. The subgraph is then used to make an arrow image scroll diagonally.
 

![](https://docs-assets.developer.apple.com/published/f428eb52efafac8ced34216d3a56ddb7/NodeGraphGraph1.png)

 Subgraph
 

![](https://docs-assets.developer.apple.com/published/86fc4df0f89268358b8fab9bbd6051f0/NodeGraphGraph2.png)

 Main material
 

 Below the texture applies to a cube.
 

[Play](#)

 A node that can contain shading nodes and other node graphs.

