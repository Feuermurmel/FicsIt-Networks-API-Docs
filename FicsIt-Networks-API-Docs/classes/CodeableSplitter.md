# Class <code>CodeableSplitter</code>

Superclasses: <a href="FGBuildableConveyorAttachment.md">FGBuildableConveyorAttachment</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>transferItem</code> (output) → transferred
Allows to transfer an item from the input queue to the given output queue if possible.

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue you want to transfer the next item to (0 = left, 1 = middle, 2 = right)
<b>Return Values:</b>

- <code><b>transferred</b></code> boolean

  true if it was able to transfer the item.
### Method <code>getInput</code> () → item
Returns the next item in the input queue.

<b>Return Values:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The next item in the input queue.
### Method <code>canOutput</code> (output) → canTransfer
Allows to check if we can transfer an item to the given output queue.

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue you want to check (0 = left, 1 = middle, 2 = right)
<b>Return Values:</b>

- <code><b>canTransfer</b></code> boolean

  True if you could transfer an item to the given output queue.
### Signal <code>ItemRequest</code> → item
Triggers when a new item is ready in the input queue.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The new item in the input queue.
### Signal <code>ItemOutputted</code> → output, item
Triggers when an item is popped from on of the output queues (aka it got transferred to a conveyor).

<b>Parameters:</b>

- <code><b>output</b></code> integer

  The index of the output queue from which the item got removed.
- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The item removed from the output queue.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>