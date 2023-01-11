# Class <code>Build_Hopper_C</code>

Superclasses: <a href="FGBuildableStorage.md">FGBuildableStorage</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_HopperMk2_C.md">Build_HopperMk2_C</a>, <a href="Build_MiniHopper_C.md">Build_MiniHopper_C</a>

Interact with the sides of the hopper to configure the item filter, then interact with the chute to extract a stack of filtered items from your inventory. 24 slot inventory.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#user-content-cycle-time">cycleTime</a>, <a href="Factory.md#user-content-max-potential">maxPotential</a>, <a href="Factory.md#user-content-min-potential">minPotential</a>, <a href="Factory.md#user-content-potential">potential</a>, <a href="Factory.md#user-content-power-consum-producing">powerConsumProducing</a>, <a href="Factory.md#user-content-productivity">productivity</a>, <a href="Factory.md#user-content-progress">progress</a>, <a href="Factory.md#user-content-standby">standby</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="get-filter-rules">getFilterRules</code> () → itemRules



<b>Return Values:</b>

- <code><b>itemRules</b></code> list of string

  
### Method <code id="get-take-or-leave">getTakeOrLeave</code> () → takeOrLeave



<b>Return Values:</b>

- <code><b>takeOrLeave</b></code> boolean

  
### Method <code id="set-take-or-leave">setTakeOrLeave</code> (takeOrLeave)


<b>Parameters:</b>

- <code><b>takeOrLeave</b></code> boolean

  

### Method <code id="remove-filter-rule">removeFilterRule</code> (itemRule) → ruleRemoved


<b>Parameters:</b>

- <code><b>itemRule</b></code> string

  

<b>Return Values:</b>

- <code><b>ruleRemoved</b></code> boolean

  
### Method <code id="add-filter-rule">addFilterRule</code> (itemRule) → ruleAdded


<b>Parameters:</b>

- <code><b>itemRule</b></code> string

  

<b>Return Values:</b>

- <code><b>ruleAdded</b></code> boolean

  
### Method <code id="clear-filter-rules">clearFilterRules</code> ()



### Method <code id="get-take-fullest">getTakeFullest</code> () → takeFullest



<b>Return Values:</b>

- <code><b>takeFullest</b></code> boolean

  
### Method <code id="set-take-fullest">setTakeFullest</code> (takeFullest)


<b>Parameters:</b>

- <code><b>takeFullest</b></code> boolean

  

### Method <code id="get-stacks-to-take">getStacksToTake</code> () → stacksToTake



<b>Return Values:</b>

- <code><b>stacksToTake</b></code> integer

  
### Method <code id="set-stacks-to-take">setStacksToTake</code> (stacksToTake)


<b>Parameters:</b>

- <code><b>stacksToTake</b></code> integer

  

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>