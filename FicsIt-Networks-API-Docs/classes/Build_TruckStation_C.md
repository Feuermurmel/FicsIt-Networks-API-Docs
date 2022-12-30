# Class <code>Build_TruckStation_C</code>

Superclasses: <a href="DockingStation.md">DockingStation</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Either send or receive resources to vehicles. Has an inventory with 48 slots.
Transfers up to 120 stacks per minute to/from docked vehicle. 
Always refuels vehicles if it has access to a matching fuel type.

## Instance Members
<b>Inherited Members:</b>
- DockingStation: <a href="DockingStation.md#getDocked">getDocked()</a>, <a href="DockingStation.md#getFuelInv">getFuelInv()</a>, <a href="DockingStation.md#getInv">getInv()</a>, <a href="DockingStation.md#isLoadMode">isLoadMode</a>, <a href="DockingStation.md#isLoadUnloading">isLoadUnloading</a>, <a href="DockingStation.md#undock">undock()</a>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>