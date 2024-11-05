# Class <code>PowerCircuit</code>

Superclasses: <a href="Object.md">Object</a>

A Object that represents a whole power circuit.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="production">production</code> float

  The amount of power produced by the whole circuit in the last tick.
- <code id="consumption">consumption</code> float

  The power consumption of the whole circuit in thge last tick.
- <code id="capacity">capacity</code> float

  The power capacity of the whole network in the last tick. (The max amount of power available in the last tick)
- <code id="battery-input">batteryInput</code> float

  The power that gone into batteries in the last tick.
- <code id="max-power-consumption">maxPowerConsumption</code> float

  The maximum consumption of power in the last tick.
- <code id="is-fuesed">isFuesed</code> boolean

  True if the fuse in the network triggered.
- <code id="has-batteries">hasBatteries</code> boolean

  True if the power circuit has batteries connected to it.
- <code id="battery-capacity">batteryCapacity</code> float

  The energy capacity all batteries of the network combined provide.
- <code id="battery-store">batteryStore</code> float

  The amount of energy currently stored in all battereies of the network combined.
- <code id="battery-store-percent">batteryStorePercent</code> float

  The fill status in percent of all battereies of the network combined.
- <code id="battery-time-until-full">batteryTimeUntilFull</code> float

  The time in seconds until every battery in the network is filled.
- <code id="battery-time-until-empty">batteryTimeUntilEmpty</code> float

  The time in seconds until every battery in the network is empty.
- <code id="battery-in">batteryIn</code> float

  The amount of energy that currently gets stored in every battery of the whole network.
- <code id="battery-out">batteryOut</code> float

  The amount of energy that currently discharges from every battery in the whole network.
### Signal <code id="-power-fuse-changed">PowerFuseChanged</code>
Get Triggered when the fuse state of the power circuit changes.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>