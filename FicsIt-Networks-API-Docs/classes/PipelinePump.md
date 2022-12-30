# Class <code>PipelinePump</code>

Superclasses: <a href="FGBuildablePipelineAttachment.md">FGBuildablePipelineAttachment</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A building that can pump fluids to a higher level within a pipeline.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>maxHeadlift</b></code> float

  The maximum amount of head lift this pump can provide.
- <code><b>designedHeadlift</b></code> float

  The amount of head lift this pump is designed for.
- <code><b>indicatorHeadlift</b></code> float

  The amount of head lift the indicator shows.
- <code><b>indicatorHeadliftPct</b></code> float

  The amount of head lift the indicator shows as percentage from max.
- <code><b>userFlowLimit</b></code> float

  The flow limit of this pump the user can specify. Use -1 for now user set limit. (in m^3/s)
- <code><b>flowLimit</b></code> float

  The overall flow limit of this pump. (in m^3/s)
- <code><b>flowLimitPct</b></code> float

  The overall flow limit of this pump. (in percent)
- <code><b>flow</b></code> float

  The current flow amount. (in m^3/s)
- <code><b>flowPct</b></code> float

  The current flow amount. (in percent)
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>