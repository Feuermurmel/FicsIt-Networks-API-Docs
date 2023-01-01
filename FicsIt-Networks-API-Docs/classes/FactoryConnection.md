# Class <code>FactoryConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that is a connection point to which a conveyor or pipe can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>type</b></code> integer

  Returns the type of the connection. 0 = Conveyor, 1 = Pipe
- <code><b>direction</b></code> integer

  The direction in which the items/fluids flow. 0 = Input, 1 = Output, 2 = Any, 3 = Used just as snap point
- <code><b>isConnected</b></code> boolean

  True if something is connected to this connection.
### Method <code>getInventory</code> () → inventory
Returns the internal inventory of the connection component.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The internal inventory of the connection component.
### Method <code>getConnected</code> () → connected
Returns the connected factory connection component.


<b>Return Values:</b>

- <code><b>connected</b></code> <a href="Inventory.md">Inventory</a>

  The connected factory connection component.
### Signal <code>ItemTransfer</code> → item
Triggers when the factory connection component transfers an item.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The transferred item
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>