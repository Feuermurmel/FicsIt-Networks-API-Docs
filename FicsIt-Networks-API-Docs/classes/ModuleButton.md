# Class <code>ModuleButton</code>

Superclasses: <a href="FINModuleBase.md">FINModuleBase</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This Button Module for modular I/O Panels can have different knob color and brightnesses and you can use them to trigger specific programmed events.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>setColor</code> (red, green, blue, Emit) → 


<b>Parameters:</b>

- <code><b>red</b></code> float

  
- <code><b>green</b></code> float

  
- <code><b>blue</b></code> float

  
- <code><b>Emit</b></code> float

  

### Method <code>trigger</code> () → 
Triggers a button press by code.


### Signal <code>Trigger</code> → 
Triggers when the button gets pressed.

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>