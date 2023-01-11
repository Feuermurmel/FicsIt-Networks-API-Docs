# Class <code>Build_PowerStorageMk1_C</code>

Superclasses: <a href="PowerStorage.md">PowerStorage</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Storage Capacity: 100 MWh (100 MW for 1 hour)
Max Charge Rate: 100 MW
Max Discharge Rate: Unlimited 

Can be connected to a Power Grid to store excess power production. The stored power can be used later in cases of high consumption.
## Instance Members
<b>Inherited Members:</b>
- PowerStorage: <a href="PowerStorage.md#user-content-battery-max-indicator-level">batteryMaxIndicatorLevel</a>, <a href="PowerStorage.md#user-content-battery-status">batteryStatus</a>, <a href="PowerStorage.md#user-content-power-capacity">powerCapacity</a>, <a href="PowerStorage.md#user-content-power-in">powerIn</a>, <a href="PowerStorage.md#user-content-power-out">powerOut</a>, <a href="PowerStorage.md#user-content-power-store">powerStore</a>, <a href="PowerStorage.md#user-content-power-store-percent">powerStorePercent</a>, <a href="PowerStorage.md#user-content-time-until-empty">timeUntilEmpty</a>, <a href="PowerStorage.md#user-content-time-until-full">timeUntilFull</a>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>