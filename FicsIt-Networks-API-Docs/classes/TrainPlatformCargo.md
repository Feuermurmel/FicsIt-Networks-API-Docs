# Class <code>TrainPlatformCargo</code>

Superclasses: <a href="TrainPlatform.md">TrainPlatform</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A train platform that allows for loading and unloading cargo cars.
## Instance Members
<b>Inherited Members:</b>
- TrainPlatform: <a href="TrainPlatform.md#user-content-get-connected-platform">getConnectedPlatform()</a>, <a href="TrainPlatform.md#user-content-get-docked-locomotive">getDockedLocomotive()</a>, <a href="TrainPlatform.md#user-content-get-docked-vehicle">getDockedVehicle()</a>, <a href="TrainPlatform.md#user-content-get-master">getMaster()</a>, <a href="TrainPlatform.md#user-content-get-track-graph">getTrackGraph()</a>, <a href="TrainPlatform.md#user-content-get-track-pos">getTrackPos()</a>, <a href="TrainPlatform.md#user-content-is-reversed">isReversed</a>, <a href="TrainPlatform.md#user-content-status">status</a>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-loading">isLoading</code> boolean

  True if the cargo platform is currently loading the docked cargo vehicle.
- <code id="is-unloading">isUnloading</code> boolean

  True if the cargo platform is currently unloading the docked cargo vehicle.
- <code id="docked-offset">dockedOffset</code> float

  The offset to the track start of the platform at were the vehicle docked.
- <code id="output-flow">outputFlow</code> float

  The current output flow rate.
- <code id="input-flow">inputFlow</code> float

  The current input flow rate.
- <code id="full-load">fullLoad</code> boolean

  True if the docked cargo vehicle is fully loaded.
- <code id="full-unload">fullUnload</code> boolean

  Ture if the docked cargo vehicle is fully unloaded.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>