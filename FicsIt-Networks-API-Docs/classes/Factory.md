# Class <code>Factory</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The base class of most machines you can build.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>progress</b></code> float

  The current production progress of the current production cycle.
- <code><b>powerConsumProducing</b></code> float

  The power consumption when producing.
- <code><b>productivity</b></code> float

  The productivity of this factory.
- <code><b>cycleTime</b></code> float

  The time that passes till one production cycle is finished.
- <code><b>maxPotential</b></code> float

  The maximum potential this factory can be set to.
- <code><b>minPotential</b></code> float

  The minimum potential this factory needs to be set to.
- <code><b>standby</b></code> boolean

  True if the factory is in standby.
- <code><b>potential</b></code> float

  The potential this factory is currently set to. (the overclock value)
 0 = 0%, 1 = 100%
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>