# Class <code>PowerStorage</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A building that can store power for later usage.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="power-store">powerStore</code> float

  The current amount of energy stored in the storage.
- <code id="power-capacity">powerCapacity</code> float

  The amount of energy the storage can hold max.
- <code id="power-store-percent">powerStorePercent</code> float

  The current power store in percent.
- <code id="power-in">powerIn</code> float

  The amount of power coming into the storage.
- <code id="power-out">powerOut</code> float

  The amount of power going out from the storage.
- <code id="time-until-full">timeUntilFull</code> float

  The time in seconds until the storage is filled.
- <code id="time-until-empty">timeUntilEmpty</code> float

  The time in seconds until the storage is empty.
- <code id="battery-status">batteryStatus</code> integer

  The current status of the battery.
0 = Idle, 1 = Idle Empty, 2 = Idle Full, 3 = Power In, 4 = Power Out
- <code id="battery-max-indicator-level">batteryMaxIndicatorLevel</code> integer

  The maximum count of Level lights that are shown.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>