# Class <code>NetworkRouter_C</code>

Superclasses: <a href="NetworkRouter.md">NetworkRouter</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The FICSIT-Networks Network Router allows you to separate two different component network from each other.
But it still lets network messages sent by network cards through.
This allows for better networking capabilities, faster networking (can reduce game lag) and makes working with larger networks and multiple computer more easy.

The router also provides a couple of functions which allow you to create filters for ports and message senders.
## Instance Members
<b>Inherited Members:</b>
- NetworkRouter: <a href="NetworkRouter.md#addAddrList">addAddrList()</a>, <a href="NetworkRouter.md#addPortList">addPortList()</a>, <a href="NetworkRouter.md#getAddrList">getAddrList()</a>, <a href="NetworkRouter.md#getPortList">getPortList()</a>, <a href="NetworkRouter.md#isAddrWhitelist">isAddrWhitelist</a>, <a href="NetworkRouter.md#isWhitelist">isWhitelist</a>, <a href="NetworkRouter.md#removeAddrList">removeAddrList()</a>, <a href="NetworkRouter.md#removePortList">removePortList()</a>, <a href="NetworkRouter.md#setAddrList">setAddrList()</a>, <a href="NetworkRouter.md#setPortList">setPortList()</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>