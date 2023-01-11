# Class <code>NetworkRouter_C</code>

Superclasses: <a href="NetworkRouter.md">NetworkRouter</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The FICSIT-Networks Network Router allows you to separate two different component network from each other.
But it still lets network messages sent by network cards through.
This allows for better networking capabilities, faster networking (can reduce game lag) and makes working with larger networks and multiple computer more easy.

The router also provides a couple of functions which allow you to create filters for ports and message senders.
## Instance Members
<b>Inherited Members:</b>
- NetworkRouter: <a href="NetworkRouter.md#user-content-add-addr-list">addAddrList()</a>, <a href="NetworkRouter.md#user-content-add-port-list">addPortList()</a>, <a href="NetworkRouter.md#user-content-get-addr-list">getAddrList()</a>, <a href="NetworkRouter.md#user-content-get-port-list">getPortList()</a>, <a href="NetworkRouter.md#user-content-is-addr-whitelist">isAddrWhitelist</a>, <a href="NetworkRouter.md#user-content-is-whitelist">isWhitelist</a>, <a href="NetworkRouter.md#user-content-remove-addr-list">removeAddrList()</a>, <a href="NetworkRouter.md#user-content-remove-port-list">removePortList()</a>, <a href="NetworkRouter.md#user-content-set-addr-list">setAddrList()</a>, <a href="NetworkRouter.md#user-content-set-port-list">setPortList()</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>