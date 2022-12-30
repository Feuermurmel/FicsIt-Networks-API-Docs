# Class <code>PipeConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that is a connection point to which a conveyor or pipe can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isConnected</b></code> boolean

  True if something is connected to this connection.
- <code><b>fluidBoxContent</b></code> float

  Returns the amount of fluid this fluid container contains
- <code><b>fluidBoxHeight</b></code> float

  Returns the height of this fluid container
- <code><b>fluidBoxLaminarHeight</b></code> float

  Returns the laminar height of this fluid container
- <code><b>fluidBoxFlowThrough</b></code> float

  Returns the amount of fluid flowing through this fluid container
- <code><b>fluidBoxFlowFill</b></code> float

  Returns the fill rate of this fluid container
- <code><b>fluidBoxFlowDrain</b></code> float

  Returns the drain rate of this fluid container
- <code><b>fluidBoxFlowLimit</b></code> float

  Returns the the maximum flow limit of this fluid container
- <code><b>networkID</b></code> integer

  Returns the network ID of the pipe network this connection is associated with
### Method <code>getFluidDescriptor</code> () → fluidDescriptor
?

<b>Return Values:</b>

- <code><b>fluidDescriptor</b></code> <a href="ItemType.md">ItemType</a>

  ?
### Method <code>flushPipeNetwork</code> () → 
Flush the associated pipe network

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>