# Class <code>FactoryConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that is a connection point to which a conveyor or pipe can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="type">type</code> integer

  Returns the type of the connection. 0 = Conveyor, 1 = Pipe
- <code id="direction">direction</code> integer

  The direction in which the items/fluids flow. 0 = Input, 1 = Output, 2 = Any, 3 = Used just as snap point
- <code id="is-connected">isConnected</code> boolean

  True if something is connected to this connection.
### Method <code id="get-inventory">getInventory</code> () → inventory
Returns the internal inventory of the connection component.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The internal inventory of the connection component.
### Method <code id="get-connected">getConnected</code> () → connected
Returns the connected factory connection component.


<b>Return Values:</b>

- <code><b>connected</b></code> <a href="Inventory.md">Inventory</a>

  The connected factory connection component.
### Signal <code id="-item-transfer">ItemTransfer</code> → item
Triggers when the factory connection component transfers an item.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The transfered item
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>