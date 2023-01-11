# Class <code>LightSource</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_CeilingLight_C.md">Build_CeilingLight_C</a>, <a href="Build_StreetLight_C.md">Build_StreetLight_C</a>, <a href="FGBuildableFloodlight.md">FGBuildableFloodlight</a>

The base class for all light you can build.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-light-enabled">isLightEnabled</code> boolean

  True if the light is enabled
- <code id="is-time-of-day-aware">isTimeOfDayAware</code> boolean

  True if the light should automatically turn on and off depending on the time of the day.
- <code id="intensity">intensity</code> float

  The intensity of the light.
- <code id="color-slot">colorSlot</code> integer

  The color slot the light uses.
### Method <code id="get-color-from-slot">getColorFromSlot</code> (slot) → color
Returns the light color that is referenced by the given slot.

<b>Parameters:</b>

- <code><b>slot</b></code> integer

  The slot you want to get the referencing color from.

<b>Return Values:</b>

- <code><b>color</b></code> <a href="../structs/Color.md">Color</a>

  The color this slot references.
### Method <code id="set-color-from-slot">setColorFromSlot</code> (slot, color)
Allows to update the light color that is referenced by the given slot.

<b>Parameters:</b>

- <code><b>slot</b></code> integer

  The slot you want to update the referencing color for.
- <code><b>color</b></code> <a href="../structs/Color.md">Color</a>

  The color this slot should now reference.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>