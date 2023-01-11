# Class <code>TimeTable</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Contains the time table information of train.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="num-stops">numStops</code> integer

  The current number of stops in the time table.
### Method <code id="add-stop">addStop</code> (index, station, ruleSet) → added
Adds a stop to the time table.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index at which the stop should get added.
- <code><b>station</b></code> <a href="RailroadStation.md">RailroadStation</a>

  The railroad station at which the stop should happen.
- <code><b>ruleSet</b></code> <a href="../structs/TrainDockingRuleSet.md">TrainDockingRuleSet</a>

  The docking rule set that describes when the train will depart from the station.

<b>Return Values:</b>

- <code><b>added</b></code> boolean

  True if the stop got successfully added to the time table.
### Method <code id="remove-stop">removeStop</code> (index)
Removes the stop with the given index from the time table.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index at which the stop should get added.

### Method <code id="get-stops">getStops</code> () → stops
Returns a list of all the stops this time table has


<b>Return Values:</b>

- <code><b>stops</b></code> list of <a href="../structs/TimeTableStop.md">TimeTableStop</a>

  A list of time table stops this time table has.
### Method <code id="set-stops">setStops</code> () → gotSet
Allows to empty and fill the stops of this time table with the given list of new stops.


<b>Return Values:</b>

- <code><b>gotSet</b></code> boolean

  True if the stops got successfully set.
### Method <code id="is-valid-stop">isValidStop</code> (index) → valid
Allows to check if the given stop index is valid.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The stop index you want to check its validity.

<b>Return Values:</b>

- <code><b>valid</b></code> boolean

  True if the stop index is valid.
### Method <code id="get-stop">getStop</code> (index) → stop
Returns the stop at the given index.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the stop you want to get.

<b>Return Values:</b>

- <code><b>stop</b></code> <a href="../structs/TimeTableStop.md">TimeTableStop</a>

  The time table stop at the given index.
### Method <code id="set-current-stop">setCurrentStop</code> (index)
Sets the stop, to which the train trys to drive to right now.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the stop the train should drive to right now.

### Method <code id="increment-current-stop">incrementCurrentStop</code> ()
Sets the current stop to the next stop in the time table.


### Method <code id="get-current-stop">getCurrentStop</code> () → index
Returns the index of the stop the train drives to right now.


<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the stop the train tries to drive to right now.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>