# Class <code>RailroadTrack</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_RailroadTrack_C.md">Build_RailroadTrack_C</a>, <a href="Build_RailroadTrackIntegrated_C.md">Build_RailroadTrackIntegrated_C</a>

A peice of railroad track over which trains can drive.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="length">length</code> float

  The length of the track.
- <code id="is-owned-by-platform">isOwnedByPlatform</code> boolean

  True if the track is part of/owned by a railroad platform.
### Method <code id="get-closest-track-position">getClosestTrackPosition</code> (worldPos) → track, offset, forward
Returns the closes track position from the given world position

<b>Parameters:</b>

- <code><b>worldPos</b></code> <a href="../structs/Vector.md">Vector</a>

  The world position form which you want to get the closest track position.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code id="get-world-loc-and-rot-at-pos">getWorldLocAndRotAtPos</code> (track, offset, forward) → location, rotation
Returns the world location and world rotation of the track position from the given track position.

<b>Parameters:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction

<b>Return Values:</b>

- <code><b>location</b></code> <a href="../structs/Vector.md">Vector</a>

  The location at the given track position
- <code><b>rotation</b></code> <a href="../structs/Vector.md">Vector</a>

  The rotation at the given track position (forward vector)
### Method <code id="get-connection">getConnection</code> (direction) → connection
Returns the railroad track connection at the given direction.

<b>Parameters:</b>

- <code><b>direction</b></code> integer

  The direction of which you want to get the connector from. 0 = front, 1 = back

<b>Return Values:</b>

- <code><b>connection</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The connection component in the given direction.
### Method <code id="get-track-graph">getTrackGraph</code> () → track
Returns the track graph of which this track is part of.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this track is part of.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>