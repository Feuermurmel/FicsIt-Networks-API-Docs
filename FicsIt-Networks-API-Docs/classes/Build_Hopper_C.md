# Class <code>Build_Hopper_C</code>

Superclasses: <a href="FGBuildableStorage.md">FGBuildableStorage</a> < <a href="Factory.md">Factory</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Interact with the sides of the hopper to configure the item filter, then interact with the chute to extract a stack of filtered items from your inventory. 24 slot inventory.
## Instance Members
<b>Inherited Members:</b>
- Factory: <a href="Factory.md#cycleTime">cycleTime</a>, <a href="Factory.md#maxPotential">maxPotential</a>, <a href="Factory.md#minPotential">minPotential</a>, <a href="Factory.md#potential">potential</a>, <a href="Factory.md#powerConsumProducing">powerConsumProducing</a>, <a href="Factory.md#productivity">productivity</a>, <a href="Factory.md#progress">progress</a>, <a href="Factory.md#standby">standby</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getFilterRules</code> () → itemRules


<b>Return Values:</b>

- <code><b>itemRules</b></code> list of string

  
### Method <code>getTakeOrLeave</code> () → takeOrLeave


<b>Return Values:</b>

- <code><b>takeOrLeave</b></code> boolean

  
### Method <code>setTakeOrLeave</code> (takeOrLeave) → 


<b>Parameters:</b>

- <code><b>takeOrLeave</b></code> boolean

  
### Method <code>removeFilterRule</code> (itemRule) → ruleRemoved


<b>Parameters:</b>

- <code><b>itemRule</b></code> string

  
<b>Return Values:</b>

- <code><b>ruleRemoved</b></code> boolean

  
### Method <code>addFilterRule</code> (itemRule) → ruleAdded


<b>Parameters:</b>

- <code><b>itemRule</b></code> string

  
<b>Return Values:</b>

- <code><b>ruleAdded</b></code> boolean

  
### Method <code>clearFilterRules</code> () → 


### Method <code>getTakeFullest</code> () → takeFullest


<b>Return Values:</b>

- <code><b>takeFullest</b></code> boolean

  
### Method <code>setTakeFullest</code> (takeFullest) → 


<b>Parameters:</b>

- <code><b>takeFullest</b></code> boolean

  
### Method <code>getStacksToTake</code> () → stacksToTake


<b>Return Values:</b>

- <code><b>stacksToTake</b></code> integer

  
### Method <code>setStacksToTake</code> (stacksToTake) → 


<b>Parameters:</b>

- <code><b>stacksToTake</b></code> integer

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>