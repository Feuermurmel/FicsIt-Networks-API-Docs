# Class <code>Train</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This class holds information and references about a trains (a collection of multiple railroad vehicles) and its timetable f.e.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isPlayerDriven</b></code> boolean

  True if the train is currently player driven.
- <code><b>isSelfDriving</b></code> boolean

  True if the train is currently self driving.
- <code><b>selfDrivingError</b></code> integer

  The last self driving error.
0 = No Error
1 = No Power
2 = No Time Table
3 = Invalid Next Stop
4 = Invalid Locomotive Placement
5 = No Path
- <code><b>hasTimeTable</b></code> boolean

  True if the train has currently a time table.
- <code><b>dockState</b></code> integer

  The current docking state of the train.
- <code><b>isDocked</b></code> boolean

  True if the train is currently docked.
### Method <code>getName</code> () → name
Returns the name of this train.

<b>Return Values:</b>

- <code><b>name</b></code> string

  The name of this train.
### Method <code>setName</code> (name) → 
Allows to set the name of this train.

<b>Parameters:</b>

- <code><b>name</b></code> string

  The new name of this train.
### Method <code>getTrackGraph</code> () → track
Returns the track graph of which this train is part of.

<b>Return Values:</b>

- <code><b>track</b></code> <a href="../structs/TrackGraph.md">TrackGraph</a>

  The track graph of which this train is part of.
### Method <code>setSelfDriving</code> (selfDriving) → 
Allows to set if the train should be self driving or not.

<b>Parameters:</b>

- <code><b>selfDriving</b></code> boolean

  True if the train should be self driving.
### Method <code>getMaster</code> () → master
Returns the master locomotive that is part of this train.

<b>Return Values:</b>

- <code><b>master</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The master locomotive of this train.
### Method <code>getTimeTable</code> () → timeTable
Returns the timetable of this train.

<b>Return Values:</b>

- <code><b>timeTable</b></code> <a href="TimeTable.md">TimeTable</a>

  The timetable of this train.
### Method <code>newTimeTable</code> () → timeTable
Creates and returns a new timetable for this train.

<b>Return Values:</b>

- <code><b>timeTable</b></code> <a href="TimeTable.md">TimeTable</a>

  The new timetable for this train.
### Method <code>getFirst</code> () → first
Returns the first railroad vehicle that is part of this train.

<b>Return Values:</b>

- <code><b>first</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The first railroad vehicle that is part of this train.
### Method <code>getLast</code> () → last
Returns the last railroad vehicle that is part of this train.

<b>Return Values:</b>

- <code><b>last</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The last railroad vehicle that is part of this train.
### Method <code>dock</code> () → 
Trys to dock the train to the station it is currently at.

### Method <code>getVehicles</code> () → vehicles
Returns a list of all the vehicles this train has.

<b>Return Values:</b>

- <code><b>vehicles</b></code> list of <a href="RailroadVehicle.md">RailroadVehicle</a>

  A list of all the vehicles this train has.
### Signal <code>SelfDrivingUpdate</code> → enabled
Triggers when the self driving mode of the train changes

<b>Parameters:</b>

- <code><b>enabled</b></code> boolean

  True if the train is now self driving.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>