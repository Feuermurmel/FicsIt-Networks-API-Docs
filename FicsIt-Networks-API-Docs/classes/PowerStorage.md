# Class <code>PowerStorage</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A building that can store power for later usage.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>powerStore</b></code> float

  The current amount of energy stored in the storage.
- <code><b>powerCapacity</b></code> float

  The amount of energy the storage can hold max.
- <code><b>powerStorePercent</b></code> float

  The current power store in percent.
- <code><b>powerIn</b></code> float

  The amount of power coming into the storage.
- <code><b>powerOut</b></code> float

  The amount of power going out from the storage.
- <code><b>timeUntilFull</b></code> float

  The time in seconds until the storage is filled.
- <code><b>timeUntilEmpty</b></code> float

  The time in seconds until the storage is empty.
- <code><b>batteryStatus</b></code> integer

  The current status of the battery.
0 = Idle, 1 = Idle Empty, 2 = Idle Full, 3 = Power In, 4 = Power Out
- <code><b>batteryMaxIndicatorLevel</b></code> integer

  The maximum count of Level lights that are shown.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>