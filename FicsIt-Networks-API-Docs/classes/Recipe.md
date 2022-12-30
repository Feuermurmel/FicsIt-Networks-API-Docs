# Class <code>Recipe</code>

Superclasses: <a href="Object.md">Object</a>

A struct that holds information about a recipe in its class. Means don't use it as object, use it as class type!
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>name</b></code> string

  The name of this recipe.
- <code><b>duration</b></code> float

  The duration how much time it takes to cycle the recipe once.
### Method <code>getProducts</code> () → products
Returns a array of item amounts, this recipe returns (outputs) when the recipe is processed once.

<b>Return Values:</b>

- <code><b>products</b></code> list of <a href="../structs/ItemAmount.md">ItemAmount</a>

  The products of this recipe.
### Method <code>getIngredients</code> () → ingredients
Returns a array of item amounts, this recipe needs (input) so the recipe can be processed.

<b>Return Values:</b>

- <code><b>ingredients</b></code> list of <a href="../structs/ItemAmount.md">ItemAmount</a>

  The ingredients of this recipe.