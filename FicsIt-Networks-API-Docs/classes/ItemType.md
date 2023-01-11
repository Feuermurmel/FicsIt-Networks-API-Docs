# Class <code>ItemType</code>

Superclasses: <a href="Object.md">Object</a>

The type of an item (iron plate, iron rod, leaves)
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>
### Fields
- <code id="s-form">form</code> integer

  The matter state of this resource.
1: Solid
2: Liquid
3: Gas
4: Heat
- <code id="s-energy">energy</code> float

  How much energy this resource provides if used as fuel.
- <code id="s-radioactive-decay">radioactiveDecay</code> float

  The amount of radiation this item radiates.
- <code id="s-name">name</code> string

  The name of the item.
- <code id="s-description">description</code> string

  The description of this item.
- <code id="s-max">max</code> integer

  The maximum stack size of this item.
- <code id="s-can-be-discarded">canBeDiscarded</code> boolean

  True if this item can be discarded.
- <code id="s-category">category</code> <a href="ItemCategory.md">ItemCategory</a>

  The category in which this item is in.
- <code id="s-fluid-color">fluidColor</code> <a href="../structs/Color.md">Color</a>

  The color of this fluid.