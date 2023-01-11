# Class <code>Manufacturer</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_AssemblerMk1_C.md">Build_AssemblerMk1_C</a>, <a href="Build_Blender_C.md">Build_Blender_C</a>, <a href="Build_ConstructorMk1_C.md">Build_ConstructorMk1_C</a>, <a href="Build_FoundryMk1_C.md">Build_FoundryMk1_C</a>, <a href="Build_ManufacturerMk1_C.md">Build_ManufacturerMk1_C</a>, <a href="Build_OilRefinery_C.md">Build_OilRefinery_C</a>, <a href="Build_Packager_C.md">Build_Packager_C</a>, <a href="Build_SmelterMk1_C.md">Build_SmelterMk1_C</a>, <a href="FGBuildableAutomatedWorkBench.md">FGBuildableAutomatedWorkBench</a>, <a href="FGBuildableConverter.md">FGBuildableConverter</a>, <a href="FGBuildableManufacturerVariablePower.md">FGBuildableManufacturerVariablePower</a>

The base class of every machine that uses a recipe to produce something automatically.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="get-recipe">getRecipe</code> () → recipe
Returns the currently set recipe of the manufacturer.


<b>Return Values:</b>

- <code><b>recipe</b></code> <a href="Recipe.md">Recipe</a>

  The currently set recipe.
### Method <code id="get-recipes">getRecipes</code> () → recipes
Returns the list of recipes this manufacturer can get set to and process.


<b>Return Values:</b>

- <code><b>recipes</b></code> list of <a href="Recipe.md">Recipe</a>

  The list of available recipes.
### Method <code id="set-recipe">setRecipe</code> (recipe) → gotSet
Sets the currently producing recipe of this manufacturer.

<b>Parameters:</b>

- <code><b>recipe</b></code> <a href="Recipe.md">Recipe</a>

  The recipe this manufacturer should produce.

<b>Return Values:</b>

- <code><b>gotSet</b></code> boolean

  True if the current recipe got successfully set to the new recipe.
### Method <code id="get-input-inv">getInputInv</code> () → inventory
Returns the input inventory of this manufacturer.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The input inventory of this manufacturer
### Method <code id="get-output-inv">getOutputInv</code> () → inventory
Returns the output inventory of this manufacturer.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The output inventory of this manufacturer.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>