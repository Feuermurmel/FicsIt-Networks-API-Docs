# Class <code>PowerConnection</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that allows for a connection point to the power network. Basically a point were a power cable can get attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="connections">connections</code> integer

  The amount of connections this power connection has.
- <code id="max-connections">maxConnections</code> integer

  The maximum amount of connections this power connection can handle.
### Method <code id="get-power">getPower</code> () → power
Returns the power info component of this power connection.


<b>Return Values:</b>

- <code><b>power</b></code> <a href="PowerInfo.md">PowerInfo</a>

  The power info compoent this power connection uses.
### Method <code id="get-circuit">getCircuit</code> () → circuit
Returns the power circuit to which this connection component is attached to.


<b>Return Values:</b>

- <code><b>circuit</b></code> <a href="PowerCircuit.md">PowerCircuit</a>

  The Power Circuit this connection component is attached to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>