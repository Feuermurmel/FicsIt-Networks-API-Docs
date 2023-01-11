# Class <code>WheeledVehicle</code>

Superclasses: <a href="Vehicle.md">Vehicle</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class for all vehicles that used wheels for movement.
## Instance Members
<b>Inherited Members:</b>
- Vehicle: <a href="Vehicle.md#user-content-health">health</a>, <a href="Vehicle.md#user-content-is-self-driving">isSelfDriving</a>, <a href="Vehicle.md#user-content-max-health">maxHealth</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="speed">speed</code> float

  The current forward speed of this vehicle.
- <code id="burn-ratio">burnRatio</code> float

  The amount of fuel this vehicle burns.
- <code id="wheels-on-ground">wheelsOnGround</code> integer

  The number of wheels currently on the ground.
- <code id="has-fuel">hasFuel</code> boolean

  True if the vehicle has currently fuel to drive.
- <code id="is-in-air">isInAir</code> boolean

  True if the vehicle is currently in the air.
- <code id="is-drifting">isDrifting</code> boolean

  True if the vehicle is currently drifting.
### Method <code id="get-fuel-inv">getFuelInv</code> () → inventory
Returns the inventory that contains the fuel of the vehicle.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The fuel inventory of the vehicle.
### Method <code id="get-storage-inv">getStorageInv</code> () → inventory
Returns the inventory that contains the storage of the vehicle.


<b>Return Values:</b>

- <code><b>inventory</b></code> <a href="Inventory.md">Inventory</a>

  The storage inventory of the vehicle.
### Method <code id="is-valid-fuel">isValidFuel</code> (item) → isValid
Allows to check if the given item type is a valid fuel for this vehicle.

<b>Parameters:</b>

- <code><b>item</b></code> <a href="ItemType.md">ItemType</a>

  The item type you want to check.

<b>Return Values:</b>

- <code><b>isValid</b></code> boolean

  True if the given item type is a valid fuel for this vehicle.
### Method <code id="get-current-target">getCurrentTarget</code> () → index
Returns the index of the target that the vehicle tries to move to right now.


<b>Return Values:</b>

- <code><b>index</b></code> integer

  The index of the current target.
### Method <code id="next-target">nextTarget</code> ()
Sets the current target to the next target in the list.


### Method <code id="set-current-target">setCurrentTarget</code> (index)
Sets the target with the given index as the target this vehicle tries to move to right now.

<b>Parameters:</b>

- <code><b>index</b></code> integer

  The index of the target this vehicle should move to now.

### Method <code id="get-target-list">getTargetList</code> () → targetList
Returns the list of targets/path waypoints.


<b>Return Values:</b>

- <code><b>targetList</b></code> <a href="TargetList.md">TargetList</a>

  The list of targets/path-waypoints.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>