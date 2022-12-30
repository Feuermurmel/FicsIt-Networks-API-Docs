# Class <code>ItemType</code>

Superclasses: <a href="Object.md">Object</a>

The type of an item (iron plate, iron rod, leaves)
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>form</b></code> integer

  The matter state of this resource.
1: Solid
2: Liquid
3: Gas
4: Heat
- <code><b>energy</b></code> float

  How much energy this resource provides if used as fuel.
- <code><b>radioactiveDecay</b></code> float

  The amount of radiation this item radiates.
- <code><b>name</b></code> string

  The name of the item.
- <code><b>description</b></code> string

  The description of this item.
- <code><b>max</b></code> integer

  The maximum stack size of this item.
- <code><b>canBeDiscarded</b></code> boolean

  True if this item can be discarded.
- <code><b>category</b></code> <a href="ItemCategory.md">ItemCategory</a>

  The category in which this item is in.
- <code><b>fluidColor</b></code> <a href="../structs/Color.md">Color</a>

  The color of this fluid.