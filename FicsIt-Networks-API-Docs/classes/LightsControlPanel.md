# Class <code>LightsControlPanel</code>

Superclasses: <a href="FGBuildableControlPanelHost.md">FGBuildableControlPanelHost</a> < <a href="CircuitBridge.md">CircuitBridge</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A control panel to configure multiple lights at once.
## Instance Members
<b>Inherited Members:</b>
- CircuitBridge: <a href="CircuitBridge.md#isBridgeActive">isBridgeActive</a>, <a href="CircuitBridge.md#isBridgeConnected">isBridgeConnected</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isLightEnabled</b></code> boolean

  True if the lights should be enabled
- <code><b>isTimeOfDayAware</b></code> boolean

  True if the lights should automatically turn on and off depending on the time of the day.
- <code><b>intensity</b></code> float

  The intensity of the lights.
- <code><b>colorSlot</b></code> integer

  The color slot the lights should use.
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