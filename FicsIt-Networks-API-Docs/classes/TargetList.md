# Class <code>TargetList</code>

Superclasses: <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The list of targets/path-waypoints a autonomous vehicle can drive
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getTarget</code> () → target
Returns the target struct at with the given index in the target list.

<b>Return Values:</b>

- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The TargetPoint-Struct with the given index in the target list.
### Method <code>removeTarget</code> (index) → 
Removes the target with the given index from the target list.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target point you want to remove from the target list.
### Method <code>addTarget</code> (target) → 
Adds the given target point struct at the end of the target list.

<b>Parameters:</b>

- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The target point you want to add.
### Method <code>setTarget</code> (index, target) → 
Allows to set the target at the given index to the given target point struct.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target point you want to update with the given target point struct.
- <code><b>target</b></code> <a href="../structs/TargetPoint.md">TargetPoint</a>

  The new target point struct for the given index.
### Method <code>getTargets</code> () → targets
Returns a list of target point structs of all the targets in the target point list.

<b>Return Values:</b>

- <code><b>targets</b></code> list of <a href="../structs/TargetPoint.md">TargetPoint</a>

  A list of target point structs containing all the targets of the target point list.
### Method <code>setTargets</code> (targets) → 
Removes all targets from the target point list and adds the given array of target point structs to the empty target point list.

<b>Parameters:</b>

- <code><b>targets</b></code> list of <a href="../structs/TargetPoint.md">TargetPoint</a>

  A list of target point structs you want to place into the empty target point list.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>