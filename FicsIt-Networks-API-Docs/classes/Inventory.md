# Class <code>Inventory</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that can hold multiple item stacks.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="can-rearrange">canRearrange</code> boolean

  Is true if items can be moved between the slots freely.
- <code id="item-count">itemCount</code> integer

  The absolute amount of items in the whole inventory.
- <code id="size">size</code> integer

  The count of available item stack slots this inventory has.
### Method <code id="get-stack">getStack</code> (args)
Returns the item stack at the given index.
Takes integers as input and returns the corresponding stacks.

<b>Parameters:</b>

- <code><b>args</b></code> unknown

  

### Method <code id="sort">sort</code> ()
Sorts the whole inventory. (like the middle mouse click into a inventory)


### Method <code id="flush">flush</code> ()
Removes all discardable items from the inventory completely. They will be gone! No way to get them back!


### Method <code id="can-split-stack-at-index">canSplitStackAtIndex</code> (index) → canSplit
Returns true of the stack at the given index can be split.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the item stack that you want to check if can be split.

<b>Return Values:</b>

- <code><b>canSplit</b></code> boolean

  True if the item stack can be split.
### Method <code id="split-stack-at-index">splitStackAtIndex</code> (index, itemCount)
Splits the stack at the given index into two. The passed amount of items gets transferred to the next available slot.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the slot which stack you want to split.
- <code><b>itemCount</b></code> integer

  The count of items that should get transferred to the next available slot.

### Method <code id="move-item-stack">moveItemStack</code> (fromIndex, toIndex, allowPartial) → count
Moves the stack of the given slot to another given slot. If partial is allowed, only moves as much items as possible, if not allowed, and the full stack doesnt fit onto the new slot, skips the move.

<b>Parameters:</b>

- <code><b>fromIndex</b></code> integer

  Index of the slot from where you want to take the stack.
- <code><b>toIndex</b></code> integer

  Index of the slot you want to move the stack to.
- <code><b>allowPartial</b></code> boolean

  Pass true if only partial item stack moving is allowed.

<b>Return Values:</b>

- <code><b>count</b></code> integer

  The count of items that have been moved.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>