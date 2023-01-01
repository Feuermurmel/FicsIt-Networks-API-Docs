# Class <code>MCP_Mod_PotWNum_C</code>

Superclasses: <a href="FINModuleBase.md">FINModuleBase</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This Potentiometer Module allows for input of a fixed value range and fires a signal with the new value each time the internal counter changes. This version has a readout display on it.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>autovalue</b></code> boolean

  
- <code><b>value</b></code> integer

  
- <code><b>max</b></code> integer

  
- <code><b>min</b></code> integer

  
### Method <code>setColor</code> (red, green, blue, Emit) → 


<b>Parameters:</b>

- <code><b>red</b></code> float

  
- <code><b>green</b></code> float

  
- <code><b>blue</b></code> float

  
- <code><b>Emit</b></code> float

  

### Method <code>setText</code> (Text) → 


<b>Parameters:</b>

- <code><b>Text</b></code> string

  

### Signal <code>valueChanged</code> → Value


<b>Parameters:</b>

- <code><b>Value</b></code> integer

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>