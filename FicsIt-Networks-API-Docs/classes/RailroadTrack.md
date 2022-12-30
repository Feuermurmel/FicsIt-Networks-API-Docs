# Class <code>RailroadTrack</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A piece of railroad track over which trains can drive.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>length</b></code> float

  The length of the track.
- <code><b>isOwnedByPlatform</b></code> boolean

  True if the track is part of/owned by a railroad platform.
### Method <code>getClosestTrackPosition(worldPos) -> track, offset, forward</code>
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
### Method <code>getWorldLocAndRotAtPos(track, offset, forward) -> location, rotation</code>
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
### Method <code>getConnection(direction) -> connection</code>
Returns the railroad track connection at the given direction.

<b>Parameters:</b>

- <code><b>direction</b></code> integer

  The direction of which you want to get the connector from. 0 = front, 1 = back
<b>Return Values:</b>

- <code><b>connection</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The connection component in the given direction.
### Method <code>getTrackGraph() -> track</code>
Returns the track graph of which this track is part of.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this track is part of.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>