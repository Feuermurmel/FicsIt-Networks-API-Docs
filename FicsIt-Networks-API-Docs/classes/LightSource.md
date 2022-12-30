# Class <code>LightSource</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for all light you can build.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isLightEnabled</b></code> boolean

  True if the light is enabled
- <code><b>isTimeOfDayAware</b></code> boolean

  True if the light should automatically turn on and off depending on the time of the day.
- <code><b>intensity</b></code> float

  The intensity of the light.
- <code><b>colorSlot</b></code> integer

  The color slot the light uses.
### Method <code>getColorFromSlot</code> (slot) → color
Returns the light color that is referenced by the given slot.

<b>Parameters:</b>

- <code><b>slot</b></code> integer

  The slot you want to get the referencing color from.
<b>Return Values:</b>

- <code><b>color</b></code> <a href="../structs/Color.md">Color</a>

  The color this slot references.
### Method <code>setColorFromSlot</code> (slot, color) → 
Allows to update the light color that is referenced by the given slot.

<b>Parameters:</b>

- <code><b>slot</b></code> integer

  The slot you want to update the referencing color for.
- <code><b>color</b></code> <a href="../structs/Color.md">Color</a>

  The color this slot should now reference.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>