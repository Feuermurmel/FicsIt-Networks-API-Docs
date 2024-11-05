# Class <code>Factory</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_CandyCaneDecor_C.md">Build_CandyCaneDecor_C</a>, <a href="Build_JumpPad_C.md">Build_JumpPad_C</a>, <a href="Build_LandingPad_C.md">Build_LandingPad_C</a>, <a href="Build_LookoutTower_C.md">Build_LookoutTower_C</a>, <a href="Build_Snowman_C.md">Build_Snowman_C</a>, <a href="DockingStation.md">DockingStation</a>, <a href="FGBuildableCheatFluidSink.md">FGBuildableCheatFluidSink</a>, <a href="FGBuildableCheatFluidSpawner.md">FGBuildableCheatFluidSpawner</a>, <a href="FGBuildableDroneStation.md">FGBuildableDroneStation</a>, <a href="FGBuildableFactorySimpleProducer.md">FGBuildableFactorySimpleProducer</a>, <a href="FGBuildableGenerator.md">FGBuildableGenerator</a>, <a href="FGBuildableJumppad.md">FGBuildableJumppad</a>, <a href="FGBuildablePipelineAttachment.md">FGBuildablePipelineAttachment</a>, <a href="FGBuildablePipePart.md">FGBuildablePipePart</a>, <a href="FGBuildableRadarTower.md">FGBuildableRadarTower</a>, <a href="FGBuildableResourceExtractorBase.md">FGBuildableResourceExtractorBase</a>, <a href="FGBuildableResourceSinkShop.md">FGBuildableResourceSinkShop</a>, <a href="FGBuildableSpaceElevator.md">FGBuildableSpaceElevator</a>, <a href="FGBuildableStorage.md">FGBuildableStorage</a>, <a href="FGBuildableTradingPost.md">FGBuildableTradingPost</a>, <a href="FGBuildableWindTurbine.md">FGBuildableWindTurbine</a>, <a href="Manufacturer.md">Manufacturer</a>, <a href="PipeReservoir.md">PipeReservoir</a>, <a href="PowerStorage.md">PowerStorage</a>, <a href="RailroadSwitchControl.md">RailroadSwitchControl</a>, <a href="ResourceSink.md">ResourceSink</a>, <a href="TrainPlatform.md">TrainPlatform</a>

The base class of most machines you can build.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="progress">progress</code> float

  The current production progress of the current production cycle.
- <code id="power-consum-producing">powerConsumProducing</code> float

  The power consumption when producing.
- <code id="productivity">productivity</code> float

  The productivity of this factory.
- <code id="cycle-time">cycleTime</code> float

  The time that passes till one production cycle is finsihed.
- <code id="max-potential">maxPotential</code> float

  The maximum potential this factory can be set to.
- <code id="min-potential">minPotential</code> float

  The minimum potential this factory needs to be set to.
- <code id="standby">standby</code> boolean

  True if the factory is in standby.
- <code id="potential">potential</code> float

  The potential this factory is currently set to. (the overclock value)
 0 = 0%, 1 = 100%
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>