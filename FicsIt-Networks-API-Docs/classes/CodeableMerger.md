# Class <code>CodeableMerger</code>

Superclasses: <a href="FGBuildableConveyorAttachment.md">FGBuildableConveyorAttachment</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>canOutput</b></code> boolean

  Is true if the output queue has a slot available for an item from one of the input queues.
### Method <code>transferItem</code> (input) → transferred
Allows to transfer an item from the given input queue to the output queue if possible.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue you want to transfer the next item to the output queue. (0 = right, 1 = middle, 2 = left)

<b>Return Values:</b>

- <code><b>transferred</b></code> boolean

  true if it was able to transfer the item.
### Method <code>getInput</code> (input) → item
Returns the next item in the given input queue.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue you want to check (0 = right, 1 = middle, 2 = left)

<b>Return Values:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The next item in the input queue.
### Signal <code>ItemRequest</code> → input, item
Triggers when a new item is ready in one of the input queues.

<b>Parameters:</b>

- <code><b>input</b></code> integer

  The index of the input queue at which the item is ready.
- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The new item in the input queue.
### Signal <code>ItemOutputted</code> → item
Triggers when an item is popped from the output queue (aka it got transferred to a conveyor).

<b>Parameters:</b>

- <code><b>item</b></code> <a href="../structs/Item.md">Item</a>

  The item removed from the output queue.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>