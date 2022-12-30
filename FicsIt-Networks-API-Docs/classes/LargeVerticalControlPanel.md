# Class <code>LargeVerticalControlPanel</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This large vertical modular I/O control panel allows you to attach multiple different modules on to it and use them as I/O to control you programms.

You can connect it to the FICSIT-Network.

Important to note is that every module is it's own component, that means if you want to listen to the signals, you will need to listen to each of them individually.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getModules() -> modules</code>


<b>Return Values:</b>

- <code><b>modules</b></code> list of <a href="Object.md">Object</a>

  
### Method <code>getModule(X, Y, Panel) -> Module</code>


<b>Parameters:</b>

- <code><b>X</b></code> integer

  
- <code><b>Y</b></code> integer

  
- <code><b>Panel</b></code> integer

  
<b>Return Values:</b>

- <code><b>Module</b></code> <a href="Actor.md">Actor</a>

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>