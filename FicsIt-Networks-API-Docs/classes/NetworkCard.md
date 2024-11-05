# Class <code>NetworkCard</code>

Superclasses: <a href="FINComputerModule.md">FINComputerModule</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="NetworkCard_C.md">NetworkCard_C</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="send">send</code> (receiver, port, args)
Sends a network message to the receiver with the given address on the given port. The data you want to add can be passed as additional parameters. Max amount of such parameters is 7 and they can only be nil, booleans, numbers and strings.

<b>Parameters:</b>

- <code><b>receiver</b></code> string

  The component ID as string of the component you want to send the network message to.
- <code><b>port</b></code> integer

  The port on which the network message should get sent. For outgoing network messages a port does not need to be opened.
- <code><b>args</b></code> unknown

  

### Method <code id="open">open</code> (port)
Opens the given port so the network card is able to receive network messages on the given port.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to open.

### Method <code id="close-all">closeAll</code> ()
Closes all ports of the network card so no further messages are able to get received


### Method <code id="close">close</code> (port)
Closes the given port so the network card wont receive network messages on the given port.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to close.

### Method <code id="broadcast">broadcast</code> (port, args)
Sends a network message to all components in the network message network (including networks sepperated by network routers) on the given port. The data you want to add can be passed as additional parameters. Max amount of such parameters is 7 and they can only be nil, booleans, numbers and strings.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port on which the network message should get sent. For outgoing network messages a port does not need to be opened.
- <code><b>args</b></code> unknown

  

### Signal <code id="-network-message">NetworkMessage</code> → sender, port, values
Triggers when the network card receives a network message on one of its opened ports. The additional arguments are the data that is contained within the network message.

<b>Parameters:</b>

- <code><b>sender</b></code> string

  The component id of the sender of the network message.
- <code><b>port</b></code> integer

  The port on which the network message got sent.
- <code><b>values</b></code> unknown

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>