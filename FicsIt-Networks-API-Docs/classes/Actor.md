# Class <code>Actor</code>

Superclasses: <a href="Object.md">Object</a>

This is the base class of all things that can exist within the world by them self.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>location</b></code> <a href="../structs/Vector.md">Vector</a>

  The location of the actor in the world.
- <code><b>scale</b></code> <a href="../structs/Vector.md">Vector</a>

  The scale of the actor in the world.
- <code><b>rotation</b></code> <a href="../structs/Rotator.md">Rotator</a>

  The rotation of the actor in the world.
### Method <code>getPowerConnectors</code> () → connectors
Returns a list of power connectors this actor might have.

<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="PowerConnection.md">PowerConnection</a>

  The power connectors this actor has.
### Method <code>getFactoryConnectors</code> () → connectors
Returns a list of factory connectors this actor might have.

<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="FactoryConnection.md">FactoryConnection</a>

  The factory connectors this actor has.
### Method <code>getPipeConnectors</code> () → connectors
Returns a list of pipe connectors this actor might have.

<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="PipeConnection.md">PipeConnection</a>

  The factory connectors this actor has.
### Method <code>getInventories</code> () → inventories
Returns a list of inventories this actor might have.

<b>Return Values:</b>

- <code><b>inventories</b></code> list of <a href="Inventory.md">Inventory</a>

  The inventories this actor has.
### Method <code>getNetworkConnectors</code> () → connectors
Returns the name of network connectors this actor might have.

<b>Return Values:</b>

- <code><b>connectors</b></code> list of <a href="ActorComponent.md">ActorComponent</a>

  The factory connectors this actor has.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>