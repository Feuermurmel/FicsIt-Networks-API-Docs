# Class <code>MCP_Mod_PotWNum_C</code>

Superclasses: <a href="FINModuleBase.md">FINModuleBase</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This Potentiometer Module allows for input of a fixed value range and fires a signal with the new value each time the internal counter changes. This version has a readout display on it.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="autovalue">autovalue</code> boolean

  
- <code id="value">value</code> integer

  
- <code id="max">max</code> integer

  
- <code id="min">min</code> integer

  
### Method <code id="set-color">setColor</code> (red, green, blue, Emit)


<b>Parameters:</b>

- <code><b>red</b></code> float

  
- <code><b>green</b></code> float

  
- <code><b>blue</b></code> float

  
- <code><b>Emit</b></code> float

  

### Method <code id="set-text">setText</code> (Text)


<b>Parameters:</b>

- <code><b>Text</b></code> string

  

### Signal <code id="value-changed">valueChanged</code> → Value


<b>Parameters:</b>

- <code><b>Value</b></code> integer

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>