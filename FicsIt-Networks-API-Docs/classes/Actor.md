# Class <code>Actor</code>

Superclasses: <a href="Object.md">Object</a>

Direct subclasses: <a href="FGBuildable.md">FGBuildable</a>, <a href="TargetList.md">TargetList</a>, <a href="TimeTable.md">TimeTable</a>, <a href="Train.md">Train</a>, <a href="Vehicle.md">Vehicle</a>

This is the base class of all things that can exist within the world by them self.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="location">location</code> <a href="../structs/Vector.md">Vector</a>

  The location of the actor in the world.
- <code id="scale">scale</code> <a href="../structs/Vector.md">Vector</a>

  The scale of the actor in the world.
- <code id="rotation">rotation</code> <a href="../structs/Rotator.md">Rotator</a>

  The rotation of the actor in the world.
### Method <code id="get-power-connectors">getPowerConnectors</code> () → connectors
Returns a list of power connectors this actor might have.


<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="PowerConnection.md">PowerConnection</a>

  The power connectors this actor has.
### Method <code id="get-factory-connectors">getFactoryConnectors</code> () → connectors
Returns a list of factory connectors this actor might have.


<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="FactoryConnection.md">FactoryConnection</a>

  The factory connectors this actor has.
### Method <code id="get-pipe-connectors">getPipeConnectors</code> () → connectors
Returns a list of pipe connectors this actor might have.


<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="PipeConnection.md">PipeConnection</a>

  The factory connectors this actor has.
### Method <code id="get-inventories">getInventories</code> () → inventories
Returns a list of inventories this actor might have.


<b>Return Values:</b>

- <code><b>inventories</b></code> list of <a href="Inventory.md">Inventory</a>

  The inventories this actor has.
### Method <code id="get-network-connectors">getNetworkConnectors</code> () → connectors
Returns the name of network connectors this actor might have.


<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="ActorComponent.md">ActorComponent</a>

  The factory connectors this actor has.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>