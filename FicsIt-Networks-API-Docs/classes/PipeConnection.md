# Class <code>PipeConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that is a connection point to which a conveyor or pipe can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-connected">isConnected</code> boolean

  True if something is connected to this connection.
- <code id="fluid-box-content">fluidBoxContent</code> float

  Returns the amount of fluid this fluid container contains
- <code id="fluid-box-height">fluidBoxHeight</code> float

  Returns the height of this fluid container
- <code id="fluid-box-laminar-height">fluidBoxLaminarHeight</code> float

  Returns the laminar height of this fluid container
- <code id="fluid-box-flow-through">fluidBoxFlowThrough</code> float

  Returns the amount of fluid flowing through this fluid container
- <code id="fluid-box-flow-fill">fluidBoxFlowFill</code> float

  Returns the fill rate of this fluid container
- <code id="fluid-box-flow-drain">fluidBoxFlowDrain</code> float

  Returns the drain rate of this fluid container
- <code id="fluid-box-flow-limit">fluidBoxFlowLimit</code> float

  Returns the the maximum flow limit of this fluid container
- <code id="network-i-d">networkID</code> integer

  Returns the network ID of the pipe network this connection is associated with
### Method <code id="get-fluid-descriptor">getFluidDescriptor</code> () → fluidDescriptor
?


<b>Return Values:</b>

- <code><b>fluidDescriptor</b></code> <a href="ItemType.md">ItemType</a>

  ?
### Method <code id="flush-pipe-network">flushPipeNetwork</code> ()
Flush the associated pipe network


## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>