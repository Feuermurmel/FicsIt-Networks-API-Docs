# Class <code>RailroadTrackConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

This is a actor component for railroad tracks that allows to connecto to other track connections and so to connection multiple tracks with each eather so you can build a train network.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="connector-location">connectorLocation</code> <a href="../structs/Vector.md">Vector</a>

  The world location of the the connection.
- <code id="connector-normal">connectorNormal</code> <a href="../structs/Vector.md">Vector</a>

  The normal vecotr of the connector.
- <code id="is-connected">isConnected</code> boolean

  True if the connection has any connection to other connections.
- <code id="is-facing-switch">isFacingSwitch</code> boolean

  True if this connection is pointing to the merge/spread point of the switch.
- <code id="is-trailing-switch">isTrailingSwitch</code> boolean

  True if this connection is pointing away from the merge/spread point of a switch.
- <code id="num-switch-positions">numSwitchPositions</code> integer

  Returns the number of different switch poisitions this switch can have.
### Method <code id="get-connection">getConnection</code> (index) → connection
Returns the connected connection with the given index.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the connected connection you want to get.

<b>Return Values:</b>

- <code><b>connection</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The connected connection at the given index.
### Method <code id="get-connections">getConnections</code> () → connections
Returns a list of all connected connections.


<b>Return Values:</b>

- <code><b>connections</b></code> list of <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  A list of all connected connections.
### Method <code id="get-track-pos">getTrackPos</code> () → track, offset, forward
Returns the track pos at which this connection is.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track the track pos points to.
- <code><b>offset</b></code> float

  The offset of the track pos.
- <code><b>forward</b></code> float

  The forward direction of the track pos. 1 = with the track direction, -1 = against the track direction
### Method <code id="get-track">getTrack</code> () → track
Returns the track of which this connection is part of.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="RailroadTrack.md">RailroadTrack</a>

  The track of which this connection is part of.
### Method <code id="get-switch-control">getSwitchControl</code> () → switchControl
Returns the switch control of this connection.


<b>Return Values:</b>

- <code><b>switchControl</b></code> <a href="RailroadSwitchControl.md">RailroadSwitchControl</a>

  The switch control of this connection.
### Method <code id="get-station">getStation</code> () → station
Returns the station of which this connection is part of.


<b>Return Values:</b>

- <code><b>station</b></code> <a href="RailroadStation.md">RailroadStation</a>

  The station of which this connection is part of.
### Method <code id="get-facing-signal">getFacingSignal</code> () → signal
Returns the signal this connection is facing to.


<b>Return Values:</b>

- <code><b>signal</b></code> <a href="RailroadSignal.md">RailroadSignal</a>

  The signal this connection is facing.
### Method <code id="get-trailing-signal">getTrailingSignal</code> () → signal
Returns the signal this connection is trailing from.


<b>Return Values:</b>

- <code><b>signal</b></code> <a href="RailroadSignal.md">RailroadSignal</a>

  The signal this connection is trailing.
### Method <code id="get-opposite">getOpposite</code> () → opposite
Returns the opposite connection of the track this connection is part of.


<b>Return Values:</b>

- <code><b>opposite</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The opposite connection of the track this connection is part of.
### Method <code id="get-next">getNext</code> () → next
Returns the next connection in the direction of the track. (used the correct path switched point to)


<b>Return Values:</b>

- <code><b>next</b></code> <a href="RailroadTrackConnection.md">RailroadTrackConnection</a>

  The next connection in the direction of the track.
### Method <code id="set-switch-position">setSwitchPosition</code> (index)
Sets the position (connection index) to which the track switch points to.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The connection index to which the switch should point to.

### Method <code id="get-switch-position">getSwitchPosition</code> () → index
Returns the current switch position.


<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the connection connection the switch currently points to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>