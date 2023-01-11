# Class <code>LightsControlPanel</code>

Superclasses: <a href="FGBuildableControlPanelHost.md">FGBuildableControlPanelHost</a> < <a href="CircuitBridge.md">CircuitBridge</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_LightsControlPanel_C.md">Build_LightsControlPanel_C</a>

A control panel to configure multiple lights at once.
## Instance Members
<b>Inherited Members:</b>
- CircuitBridge: <a href="CircuitBridge.md#user-content-is-bridge-active">isBridgeActive</a>, <a href="CircuitBridge.md#user-content-is-bridge-connected">isBridgeConnected</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-light-enabled">isLightEnabled</code> boolean

  True if the lights should be enabled
- <code id="is-time-of-day-aware">isTimeOfDayAware</code> boolean

  True if the lights should automatically turn on and off depending on the time of the day.
- <code id="intensity">intensity</code> float

  The intensity of the lights.
- <code id="color-slot">colorSlot</code> integer

  The color slot the lights should use.
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