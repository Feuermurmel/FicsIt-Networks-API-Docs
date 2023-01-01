# Class <code>PowerInfo</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that provides information and mainly statistics about the power connection it is attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>dynProduction</b></code> float

  The production capacity this connection provided last tick.
- <code><b>baseProduction</b></code> float

  The base production capacity this connection always provides.
- <code><b>maxDynProduction</b></code> float

  The maximum production capacity this connection could have provided to the circuit in the last tick.
- <code><b>targetConsumption</b></code> float

  The amount of energy the connection wanted to consume from the circuit in the last tick.
- <code><b>consumption</b></code> float

  The amount of energy the connection actually consumed in the last tick.
- <code><b>hasPower</b></code> boolean

  True if the connection has satisfied power values and counts as being powered. (True if it has power)
### Method <code>getCircuit</code> () → circuit
Returns the power circuit this info component is part of.


<b>Return Values:</b>

- <code><b>circuit</b></code> <a href="PowerCircuit.md">PowerCircuit</a>

  The Power Circuit this info component is attached to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>