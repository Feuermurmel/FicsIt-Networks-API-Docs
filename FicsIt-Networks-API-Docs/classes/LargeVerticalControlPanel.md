# Class <code>LargeVerticalControlPanel</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This large verical modular I/O control panel allows you to attach multiple different modules on to it and use them as I/O to control you programms.

You can connect it to the FicsIt-Network.

Important to note is that every module is it's own component, that means if you want to listen to the signals, you will need to listen to each of them individually.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="get-modules">getModules</code> () → modules



<b>Return Values:</b>

- <code><b>modules</b></code> list of <a href="Object.md">Object</a>

  
### Method <code id="get-module">getModule</code> (X, Y, Panel) → Module


<b>Parameters:</b>

- <code><b>X</b></code> integer

  
- <code><b>Y</b></code> integer

  
- <code><b>Panel</b></code> integer

  

<b>Return Values:</b>

- <code><b>Module</b></code> <a href="Actor.md">Actor</a>

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>