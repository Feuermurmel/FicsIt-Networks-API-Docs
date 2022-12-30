# Class <code>DockingStation</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A docking station for wheeled vehicles to transfer cargo.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isLoadMode</b></code> boolean

  True if the docking station loads docked vehicles, false if it unloads them.
- <code><b>isLoadUnloading</b></code> boolean

  True if the docking station is currently loading or unloading a docked vehicle.
### Method <code>getFuelInv</code> () → inventory
Returns the fuel inventory of the docking station.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The fuel inventory of the docking station.
### Method <code>getInv</code> () → inventory
Returns the cargo inventory of the docking station.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The cargo inventory of this docking station.
### Method <code>getDocked</code> () → docked
Returns the currently docked actor.

<b>Return Values:</b>

- <code><b>docked</b></code> <a href="Actor.md">Actor</a>

  The currently docked actor.
### Method <code>undock</code> () → 
Undocked the currently docked vehicle from this docking station.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>