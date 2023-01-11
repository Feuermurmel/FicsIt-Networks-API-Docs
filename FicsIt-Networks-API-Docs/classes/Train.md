# Class <code>Train</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This class holds information and references about a trains (a collection of multiple railroad vehicles) and its timetable f.e.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-player-driven">isPlayerDriven</code> boolean

  True if the train is currently player driven.
- <code id="is-self-driving">isSelfDriving</code> boolean

  True if the train is currently self driving.
- <code id="self-driving-error">selfDrivingError</code> integer

  The last self driving error.
0 = No Error
1 = No Power
2 = No Time Table
3 = Invalid Next Stop
4 = Invalid Locomotive Placement
5 = No Path
- <code id="has-time-table">hasTimeTable</code> boolean

  True if the train has currently a time table.
- <code id="dock-state">dockState</code> integer

  The current docking state of the train.
- <code id="is-docked">isDocked</code> boolean

  True if the train is currently docked.
### Method <code id="get-name">getName</code> () → name
Returns the name of this train.


<b>Return Values:</b>

- <code><b>name</b></code> string

  The name of this train.
### Method <code id="set-name">setName</code> (name)
Allows to set the name of this train.

<b>Parameters:</b>

- <code><b>name</b></code> string

  The new name of this train.

### Method <code id="get-track-graph">getTrackGraph</code> () → track
Returns the track graph of which this train is part of.


<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this train is part of.
### Method <code id="set-self-driving">setSelfDriving</code> (selfDriving)
Allows to set if the train should be self driving or not.

<b>Parameters:</b>

- <code><b>selfDriving</b></code> boolean

  True if the train should be self driving.

### Method <code id="get-master">getMaster</code> () → master
Returns the master locomotive that is part of this train.


<b>Return Values:</b>

- <code><b>master</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The master locomotive of this train.
### Method <code id="get-time-table">getTimeTable</code> () → timeTable
Returns the timetable of this train.


<b>Return Values:</b>

- <code><b>timeTable</b></code> <a href="TimeTable.md">TimeTable</a>

  The timetable of this train.
### Method <code id="new-time-table">newTimeTable</code> () → timeTable
Creates and returns a new timetable for this train.


<b>Return Values:</b>

- <code><b>timeTable</b></code> <a href="TimeTable.md">TimeTable</a>

  The new timetable for this train.
### Method <code id="get-first">getFirst</code> () → first
Returns the first railroad vehicle that is part of this train.


<b>Return Values:</b>

- <code><b>first</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The first railroad vehicle that is part of this train.
### Method <code id="get-last">getLast</code> () → last
Returns the last railroad vehicle that is part of this train.


<b>Return Values:</b>

- <code><b>last</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The last railroad vehicle that is part of this train.
### Method <code id="dock">dock</code> ()
Trys to dock the train to the station it is currently at.


### Method <code id="get-vehicles">getVehicles</code> () → vehicles
Returns a list of all the vehicles this train has.


<b>Return Values:</b>

- <code><b>vehicles</b></code> list of <a href="RailroadVehicle.md">RailroadVehicle</a>

  A list of all the vehicles this train has.
### Signal <code id="-self-driving-update">SelfDrivingUpdate</code> → enabled
Triggers when the self driving mode of the train changes

<b>Parameters:</b>

- <code><b>enabled</b></code> boolean

  True if the train is now self driving.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>