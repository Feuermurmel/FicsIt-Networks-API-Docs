# Class <code>PipeReservoir</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_IndustrialTank_C.md">Build_IndustrialTank_C</a>, <a href="Build_PipeStorageTank_C.md">Build_PipeStorageTank_C</a>

The base class for all fluid tanks.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="fluid-content">fluidContent</code> float

  The amount of fluid in the tank.
- <code id="max-fluid-content">maxFluidContent</code> float

  The maximum amount of fluid this tank can hold.
- <code id="flow-fill">flowFill</code> float

  The current inflow rate of fluid.
- <code id="flow-drain">flowDrain</code> float

  The current outflow rate of fluid.
- <code id="flow-limit">flowLimit</code> float

  The maximum flow rate of fluid this tank can handle.
### Method <code id="flush">flush</code> ()
Empties the whole fluid container.


### Method <code id="get-fluid-type">getFluidType</code> () → type
Returns the type of the fluid.


<b>Return Values:</b>

- <code><b>type</b></code> <a href="ItemType.md">ItemType</a>

  The type of the fluid the tank contains.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>