# Class <code>TargetList</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The list of targets/path-waypoints a autonomous vehicle can drive
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="get-target">getTarget</code> () → target
Returns the target struct at with the given index in the target list.


<b>Return Values:</b>

- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The TargetPoint-Struct with the given index in the target list.
### Method <code id="remove-target">removeTarget</code> (index)
Removes the target with the given index from the target list.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target point you want to remove from the target list.

### Method <code id="add-target">addTarget</code> (target)
Adds the given target point struct at the end of the target list.

<b>Parameters:</b>

- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The target point you want to add.

### Method <code id="set-target">setTarget</code> (index, target)
Allows to set the target at the given index to the given target point struct.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target point you want to update with the given target point struct.
- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The new target point struct for the given index.

### Method <code id="get-targets">getTargets</code> () → targets
Returns a list of target point structs of all the targets in the target point list.


<b>Return Values:</b>

- <code><b>targets</b></code> list of <a href="../structs/TargetPoint.md">TargetPoint</a>

  A list of target point structs containing all the targets of the target point list.
### Method <code id="set-targets">setTargets</code> (targets)
Removes all targets from the target point list and adds the given array of target point structs to the empty target point list.

<b>Parameters:</b>

- <code><b>targets</b></code> list of <a href="../structs/TargetPoint.md">TargetPoint</a>

  A list of target point structs you want to place into the empty target point list.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>