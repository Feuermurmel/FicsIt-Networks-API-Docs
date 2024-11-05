# Class <code>PowerInfo</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

A actor component that provides information and mainly statistics about the power connection it is attached to.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="dyn-production">dynProduction</code> float

  The production cpacity this connection provided last tick.
- <code id="base-production">baseProduction</code> float

  The base production capactiy this connection always provides.
- <code id="max-dyn-production">maxDynProduction</code> float

  The maximum production capactiy this connection could have provided to the circuit in the last tick.
- <code id="target-consumption">targetConsumption</code> float

  The amount of energy the connection wanted to consume from the circuit in the last tick.
- <code id="consumption">consumption</code> float

  The amount of energy the connection actually consumed in the last tick.
- <code id="has-power">hasPower</code> boolean

  True if the connection has satisfied power values and counts as beeing powered. (True if it has power)
### Method <code id="get-circuit">getCircuit</code> () → circuit
Returns the power circuit this info component is part of.


<b>Return Values:</b>

- <code><b>circuit</b></code> <a href="PowerCircuit.md">PowerCircuit</a>

  The Power Circuit this info component is attached to.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>