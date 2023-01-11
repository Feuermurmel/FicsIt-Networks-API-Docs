# Class <code>CodeableSplitter</code>

Superclasses: <a href="FGBuildableConveyorAttachment.md">FGBuildableConveyorAttachment</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="CodeableSplitter_C.md">CodeableSplitter_C</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="transfer-item">transferItem</code> (output) → transferred
Allows to transfer an item from the input queue to the given output queue if possible.

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue you want to transfer the next item to (0 = left, 1 = middle, 2 = right)

<b>Return Values:</b>

- <code><b>transferred</b></code> boolean

  true if it was able to transfer the item.
### Method <code id="get-input">getInput</code> () → item
Returns the next item in the input queue.


<b>Return Values:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The next item in the input queue.
### Method <code id="can-output">canOutput</code> (output) → canTransfer
Allows to check if we can transfer an item to the given output queue.

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue you want to check (0 = left, 1 = middle, 2 = right)

<b>Return Values:</b>

- <code><b>canTransfer</b></code> boolean

  True if you could transfer an item to the given output queue.
### Signal <code id="-item-request">ItemRequest</code> → item
Triggers when a new item is ready in the input queue.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The new item in the input queue.
### Signal <code id="-item-outputted">ItemOutputted</code> → output, item
Triggers when an item is popped from on of the output queues (aka it got transferred to a conveyor).

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue from which the item got removed.
- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The item removed from the output queue.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>