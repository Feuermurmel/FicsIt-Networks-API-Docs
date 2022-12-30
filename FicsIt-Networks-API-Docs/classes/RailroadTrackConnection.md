# Class <code>RailroadTrackConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

This is a actor component for railroad tracks that allows to connect to other track connections and so to connection multiple tracks with each other so you can build a train network.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>connectorLocation</b></code> <a href="../structs/Vector.md">Vector</a>

  The world location of the the connection.
- <code><b>connectorNormal</b></code> <a href="../structs/Vector.md">Vector</a>

  The normal vector of the connector.
- <code><b>isConnected</b></code> boolean

  True if the connection has any connection to other connections.
- <code><b>isFacingSwitch</b></code> boolean

  True if this connection is pointing to the merge/spread point of the switch.
- <code><b>isTrailingSwitch</b></code> boolean

  True if this connection is pointing away from the merge/spread point of a switch.
- <code><b>numSwitchPositions</b></code> integer

  Returns the number of different switch positions this switch can have.
### Method <code>getConnection(index) -> connection</code>
Returns the connected connection with the given index.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the connected connection you want to get.
<b>Return Values:</b>

- <code><b>connection</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The connected connection at the given index.
### Method <code>getConnections() -> connections</code>
Returns a list of all connected connections.

<b>Return Values:</b>

- <code><b>connections</b></code> list of <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  A list of all connected connections.
### Method <code>getTrackPos() -> track, offset, forward</code>
Returns the track pos at which this connection is.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code>getTrack() -> track</code>
Returns the track of which this connection is part of.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track of which this connection is part of.
### Method <code>getSwitchControl() -> switchControl</code>
Returns the switch control of this connection.

<b>Return Values:</b>

- <code><b>switchControl</b></code> <a href="RailroadSwitchControl.md">RailroadSwitchControl</a>

  The switch control of this connection.
### Method <code>getStation() -> station</code>
Returns the station of which this connection is part of.

<b>Return Values:</b>

- <code><b>station</b></code> <a href="RailroadStation.md">RailroadStation</a>

  The station of which this connection is part of.
### Method <code>getFacingSignal() -> signal</code>
Returns the signal this connection is facing to.

<b>Return Values:</b>

- <code><b>signal</b></code> <a href="RailroadSignal.md">RailroadSignal</a>

  The signal this connection is facing.
### Method <code>getTrailingSignal() -> signal</code>
Returns the signal this connection is trailing from.

<b>Return Values:</b>

- <code><b>signal</b></code> <a href="RailroadSignal.md">RailroadSignal</a>

  The signal this connection is trailing.
### Method <code>getOpposite() -> opposite</code>
Returns the opposite connection of the track this connection is part of.

<b>Return Values:</b>

- <code><b>opposite</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The opposite connection of the track this connection is part of.
### Method <code>getNext() -> next</code>
Returns the next connection in the direction of the track. (used the correct path switched point to)

<b>Return Values:</b>

- <code><b>next</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The next connection in the direction of the track.
### Method <code>setSwitchPosition(index) -> </code>
Sets the position (connection index) to which the track switch points to.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The connection index to which the switch should point to.
### Method <code>getSwitchPosition() -> index</code>
Returns the current switch position.

<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the connection connection the switch currently points to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>