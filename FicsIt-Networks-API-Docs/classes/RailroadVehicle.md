# Class <code>RailroadVehicle</code>

Superclasses: <a href="Vehicle.md">Vehicle</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for any vehicle that drives on train tracks.
## Instance Members
<b>Inherited Members:</b>
- Vehicle: <a href="Vehicle.md#user-content-health">health</a>, <a href="Vehicle.md#user-content-is-self-driving">isSelfDriving</a>, <a href="Vehicle.md#user-content-max-health">maxHealth</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="length">length</code> float

  The length of this vehicle on the track.
- <code id="is-docked">isDocked</code> boolean

  True if this vehicle is currently docked to a platform.
- <code id="is-reversed">isReversed</code> boolean

  True if the vehicle is placed reversed on the track.
### Method <code id="get-train">getTrain</code> () → train
Returns the train of which this vehicle is part of.


<b>Return Values:</b>

- <code><b>train</b></code> <a href="Train.md">Train</a>

  The train of which this vehicle is part of
### Method <code id="is-coupled">isCoupled</code> (coupler) → coupled
Allows to check if the given coupler is coupled to another car.

<b>Parameters:</b>

- <code><b>coupler</b></code> integer

  The Coupler you want to check. 0 = Front, 1 = Back

<b>Return Values:</b>

- <code><b>coupled</b></code> boolean

  True of the give coupler is coupled to another car.
### Method <code id="get-coupled">getCoupled</code> (coupler) → coupled
Allows to get the coupled vehicle at the given coupler.

<b>Parameters:</b>

- <code><b>coupler</b></code> integer

  The Coupler you want to get the car from. 0 = Front, 1 = Back

<b>Return Values:</b>

- <code><b>coupled</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The coupled car of the given coupler is coupled to another car.
### Method <code id="get-track-graph">getTrackGraph</code> () → track
Returns the track graph of which this vehicle is part of.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this vehicle is part of.
### Method <code id="get-track-pos">getTrackPos</code> () → track, offset, forward
Returns the track pos at which this vehicle is.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code id="get-movement">getMovement</code> () → movement
Returns the vehicle movement of this vehicle.


<b>Return Values:</b>

- <code><b>movement</b></code> <a href="RailroadVehicleMovement.md">RailroadVehicleMovement</a>

  The movement of this vehicle.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>