# Class <code>CodeableMerger</code>

Superclasses: <a href="FGBuildableConveyorAttachment.md">FGBuildableConveyorAttachment</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="can-output">canOutput</code> boolean

  Is true if the output queue has a slot available for an item from one of the input queues.
### Method <code id="transfer-item">transferItem</code> (input) → transferred
Allows to transfer an item from the given input queue to the output queue if possible.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue you want to transfer the next item to the output queue. (0 = right, 1 = middle, 2 = left)

<b>Return Values:</b>

- <code><b>transferred</b></code> boolean

  true if it was able to transfer the item.
### Method <code id="get-input">getInput</code> (input) → item
Returns the next item in the given input queue.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue you want to check (0 = right, 1 = middle, 2 = left)

<b>Return Values:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The next item in the input queue.
### Signal <code id="-item-request">ItemRequest</code> → input, item
Triggers when a new item is ready in one of the input queues.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue at which the item is ready.
- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The new item in the input queue.
### Signal <code id="-item-outputted">ItemOutputted</code> → item
Triggers when an item is popped from the output queue (aka it got transferred to a conveyor).

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The item removed from the output queue.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>