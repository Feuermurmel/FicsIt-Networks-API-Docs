# Class <code>ComputerCase</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Computer_C.md">Computer_C</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Signal <code id="-file-system-update">FileSystemUpdate</code> → type, from, to
Triggers when something in the filesystem changes.

<b>Parameters:</b>

- <code><b>type</b></code> integer

  The type of the change.
- <code><b>from</b></code> string

  The file path to the FS node that has changed.
- <code><b>to</b></code> string

  The new file path of the node if it has changed.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>