# Class <code>TimeTable</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Contains the time table information of train.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>numStops</b></code> integer

  The current number of stops in the time table.
### Method <code>addStop</code> (index, station, ruleSet) → added
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
### Method <code>removeStop</code> (index) → 
Removes the stop with the given index from the time table.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index at which the stop should get added.
### Method <code>getStops</code> () → stops
Returns a list of all the stops this time table has

<b>Return Values:</b>

- <code><b>stops</b></code> list of <a href="../structs/TimeTableStop.md">TimeTableStop</a>

  A list of time table stops this time table has.
### Method <code>setStops</code> () → gotSet
Allows to empty and fill the stops of this time table with the given list of new stops.

<b>Return Values:</b>

- <code><b>gotSet</b></code> boolean

  True if the stops got successfully set.
### Method <code>isValidStop</code> (index) → valid
Allows to check if the given stop index is valid.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The stop index you want to check its validity.
<b>Return Values:</b>

- <code><b>valid</b></code> boolean

  True if the stop index is valid.
### Method <code>getStop</code> (index) → stop
Returns the stop at the given index.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the stop you want to get.
<b>Return Values:</b>

- <code><b>stop</b></code> <a href="../structs/TimeTableStop.md">TimeTableStop</a>

  The time table stop at the given index.
### Method <code>setCurrentStop</code> (index) → 
Sets the stop, to which the train trys to drive to right now.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the stop the train should drive to right now.
### Method <code>incrementCurrentStop</code> () → 
Sets the current stop to the next stop in the time table.

### Method <code>getCurrentStop</code> () → index
Returns the index of the stop the train drives to right now.

<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the stop the train tries to drive to right now.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>