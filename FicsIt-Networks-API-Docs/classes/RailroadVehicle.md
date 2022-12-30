# Class <code>RailroadVehicle</code>

Superclasses: <a href="Vehicle.md">Vehicle</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for any vehicle that drives on train tracks.
## Instance Members
<b>Inherited Members:</b>
- Vehicle: <a href="Vehicle.md#health">health</a>, <a href="Vehicle.md#isSelfDriving">isSelfDriving</a>, <a href="Vehicle.md#maxHealth">maxHealth</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>length</b></code> float

  The length of this vehicle on the track.
- <code><b>isDocked</b></code> boolean

  True if this vehicle is currently docked to a platform.
- <code><b>isReversed</b></code> boolean

  True if the vehicle is placed reversed on the track.
### Method <code>getTrain() -> train</code>
Returns the train of which this vehicle is part of.

<b>Return Values:</b>

- <code><b>train</b></code> <a href="Train.md">Train</a>

  The train of which this vehicle is part of
### Method <code>isCoupled(coupler) -> coupled</code>
Allows to check if the given coupler is coupled to another car.

<b>Parameters:</b>

- <code><b>coupler</b></code> integer

  The Coupler you want to check. 0 = Front, 1 = Back
<b>Return Values:</b>

- <code><b>coupled</b></code> boolean

  True of the give coupler is coupled to another car.
### Method <code>getCoupled(coupler) -> coupled</code>
Allows to get the coupled vehicle at the given coupler.

<b>Parameters:</b>

- <code><b>coupler</b></code> integer

  The Coupler you want to get the car from. 0 = Front, 1 = Back
<b>Return Values:</b>

- <code><b>coupled</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The coupled car of the given coupler is coupled to another car.
### Method <code>getTrackGraph() -> track</code>
Returns the track graph of which this vehicle is part of.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this vehicle is part of.
### Method <code>getTrackPos() -> track, offset, forward</code>
Returns the track pos at which this vehicle is.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code>getMovement() -> movement</code>
Returns the vehicle movement of this vehicle.

<b>Return Values:</b>

- <code><b>movement</b></code> <a href="RailroadVehicleMovement.md">RailroadVehicleMovement</a>

  The movement of this vehicle.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>