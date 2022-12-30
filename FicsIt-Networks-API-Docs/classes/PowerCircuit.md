# Class <code>PowerCircuit</code>

Superclasses: <a href="Object.md">Object</a>

A Object that represents a whole power circuit.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>production</b></code> float

  The amount of power produced by the whole circuit in the last tick.
- <code><b>consumption</b></code> float

  The power consumption of the whole circuit in thg last tick.
- <code><b>capacity</b></code> float

  The power capacity of the whole network in the last tick. (The max amount of power available in the last tick)
- <code><b>batteryInput</b></code> float

  The power that gone into batteries in the last tick.
- <code><b>maxPowerConsumption</b></code> float

  The maximum consumption of power in the last tick.
- <code><b>isFuseTriggered</b></code> boolean

  True if the fuse in the network triggered.
- <code><b>hasBatteries</b></code> boolean

  True if the power circuit has batteries connected to it.
- <code><b>batteryCapacity</b></code> float

  The energy capacity all batteries of the network combined provide.
- <code><b>batteryStore</b></code> float

  The amount of energy currently stored in all batteries of the network combined.
- <code><b>batteryStorePercent</b></code> float

  The fill status in percent of all batteries of the network combined.
- <code><b>batteryTimeUntilFull</b></code> float

  The time in seconds until every battery in the network is filled.
- <code><b>batteryTimeUntilEmpty</b></code> float

  The time in seconds until every battery in the network is empty.
- <code><b>batteryIn</b></code> float

  The amount of energy that currently gets stored in every battery of the whole network.
- <code><b>batteryOut</b></code> float

  The amount of energy that currently discharges from every battery in the whole network.
### Signal <code>PowerFuseChanged -> </code>
Get Triggered when the fuse state of the power circuit changes.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>