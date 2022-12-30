# Class <code>Manufacturer</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class of every machine that uses a recipe to produce something automatically.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getRecipe() -> recipe</code>
Returns the currently set recipe of the manufacturer.

<b>Return Values:</b>

- <code><b>recipe</b></code> <a href="Recipe.md">Recipe</a>

  The currently set recipe.
### Method <code>getRecipes() -> recipes</code>
Returns the list of recipes this manufacturer can get set to and process.

<b>Return Values:</b>

- <code><b>recipes</b></code> list of <a href="Recipe.md">Recipe</a>

  The list of available recipes.
### Method <code>setRecipe(recipe) -> gotSet</code>
Sets the currently producing recipe of this manufacturer.

<b>Parameters:</b>

- <code><b>recipe</b></code> <a href="Recipe.md">Recipe</a>

  The recipe this manufacturer should produce.
<b>Return Values:</b>

- <code><b>gotSet</b></code> boolean

  True if the current recipe got successfully set to the new recipe.
### Method <code>getInputInv() -> inventory</code>
Returns the input inventory of this manufacturer.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The input inventory of this manufacturer
### Method <code>getOutputInv() -> inventory</code>
Returns the output inventory of this manufacturer.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The output inventory of this manufacturer.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>