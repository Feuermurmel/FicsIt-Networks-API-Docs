# Class <code>PowerConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that allows for a connection point to the power network. Basically a point were a power cable can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>connections</b></code> integer

  The amount of connections this power connection has.
- <code><b>maxConnections</b></code> integer

  The maximum amount of connections this power connection can handle.
### Method <code>getPower</code> () → power
Returns the power info component of this power connection.

<b>Return Values:</b>

- <code><b>power</b></code> <a href="PowerInfo.md">PowerInfo</a>

  The power info component this power connection uses.
### Method <code>getCircuit</code> () → circuit
Returns the power circuit to which this connection component is attached to.

<b>Return Values:</b>

- <code><b>circuit</b></code> <a href="PowerCircuit.md">PowerCircuit</a>

  The Power Circuit this connection component is attached to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>