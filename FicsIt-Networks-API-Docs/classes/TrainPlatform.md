# Class <code>TrainPlatform</code>

Superclasses: <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for all train station parts.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>status</b></code> integer

  The current docking status of the platform.
- <code><b>isReversed</b></code> boolean

  True if the orientation of the platform is reversed relative to the track/station.
### Method <code>getTrackGraph</code> () → graph
Returns the track graph of which this platform is part of.


<b>Return Values:</b>

- <code><b>graph</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this platform is part of.
### Method <code>getTrackPos</code> () → track, offset, forward
Returns the track pos at which this train platform is placed.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code>getConnectedPlatform</code> (direction) → platform
Returns the connected platform in the given direction.

<b>Parameters:</b>

- <code><b>direction</b></code> integer

  The direction in which you want to get the connected platform.

<b>Return Values:</b>

- <code><b>platform</b></code> <a href="TrainPlatform.md">TrainPlatform</a>

  The platform connected to this platform in the given direction.
### Method <code>getDockedVehicle</code> () → vehicle
Returns the currently docked vehicle.


<b>Return Values:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The currently docked vehicle
### Method <code>getMaster</code> () → master
Returns the master platform of this train station.


<b>Return Values:</b>

- <code><b>master</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The master platform of this train station.
### Method <code>getDockedLocomotive</code> () → locomotive
Returns the currently docked locomotive at the train station.


<b>Return Values:</b>

- <code><b>locomotive</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The currently docked locomotive at the train station.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>