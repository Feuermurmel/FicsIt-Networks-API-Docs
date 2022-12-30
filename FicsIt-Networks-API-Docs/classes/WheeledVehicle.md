# Class <code>WheeledVehicle</code>

Superclasses: <a href="Vehicle.md">Vehicle</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for all vehicles that used wheels for movement.
## Instance Members
<b>Inherited Members:</b>
- Vehicle: <a href="Vehicle.md#health">health</a>, <a href="Vehicle.md#isSelfDriving">isSelfDriving</a>, <a href="Vehicle.md#maxHealth">maxHealth</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>speed</b></code> float

  The current forward speed of this vehicle.
- <code><b>burnRatio</b></code> float

  The amount of fuel this vehicle burns.
- <code><b>wheelsOnGround</b></code> integer

  The number of wheels currently on the ground.
- <code><b>hasFuel</b></code> boolean

  True if the vehicle has currently fuel to drive.
- <code><b>isInAir</b></code> boolean

  True if the vehicle is currently in the air.
- <code><b>isDrifting</b></code> boolean

  True if the vehicle is currently drifting.
### Method <code>getFuelInv() -> inventory</code>
Returns the inventory that contains the fuel of the vehicle.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The fuel inventory of the vehicle.
### Method <code>getStorageInv() -> inventory</code>
Returns the inventory that contains the storage of the vehicle.

<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The storage inventory of the vehicle.
### Method <code>isValidFuel(item) -> isValid</code>
Allows to check if the given item type is a valid fuel for this vehicle.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="ItemType.md">ItemType</a>

  The item type you want to check.
<b>Return Values:</b>

- <code><b>isValid</b></code> boolean

  True if the given item type is a valid fuel for this vehicle.
### Method <code>getCurrentTarget() -> index</code>
Returns the index of the target that the vehicle tries to move to right now.

<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the current target.
### Method <code>nextTarget() -> </code>
Sets the current target to the next target in the list.

### Method <code>setCurrentTarget(index) -> </code>
Sets the target with the given index as the target this vehicle tries to move to right now.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target this vehicle should move to now.
### Method <code>getTargetList() -> targetList</code>
Returns the list of targets/path waypoints.

<b>Return Values:</b>

- <code><b>targetList</b></code> <a href="TargetList.md">TargetList</a>

  The list of targets/path-waypoints.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>