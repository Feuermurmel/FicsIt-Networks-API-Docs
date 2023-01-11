# Class <code>PipelinePump</code>

Superclasses: <a href="FGBuildablePipelineAttachment.md">FGBuildablePipelineAttachment</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A building that can pump fluids to a higher level within a pipeline.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="max-headlift">maxHeadlift</code> float

  The maximum amount of head lift this pump can provide.
- <code id="designed-headlift">designedHeadlift</code> float

  The amount of head lift this pump is designed for.
- <code id="indicator-headlift">indicatorHeadlift</code> float

  The amount of head lift the indicator shows.
- <code id="indicator-headlift-pct">indicatorHeadliftPct</code> float

  The amount of head lift the indicator shows as percentage from max.
- <code id="user-flow-limit">userFlowLimit</code> float

  The flow limit of this pump the user can specify. Use -1 for now user set limit. (in m^3/s)
- <code id="flow-limit">flowLimit</code> float

  The overall flow limit of this pump. (in m^3/s)
- <code id="flow-limit-pct">flowLimitPct</code> float

  The overall flow limit of this pump. (in percent)
- <code id="flow">flow</code> float

  The current flow amount. (in m^3/s)
- <code id="flow-pct">flowPct</code> float

  The current flow amount. (in percent)
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>