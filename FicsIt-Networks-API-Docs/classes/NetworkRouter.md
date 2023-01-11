# Class <code>NetworkRouter</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-whitelist">isWhitelist</code> boolean

  
- <code id="is-addr-whitelist">isAddrWhitelist</code> boolean

  True if the address filter list is used as whitelist.
### Method <code id="set-port-list">setPortList</code> () → ports
Overrides the port filter list with the given array.


<b>Return Values:</b>

- <code><b>ports</b></code> list of integer

  The port array you want to override the filter list with.
### Method <code id="set-addr-list">setAddrList</code> () → addresses
Overrides the address filter list with the given array.


<b>Return Values:</b>

- <code><b>addresses</b></code> list of string

  The address array you want to override the filter list with.
### Method <code id="remove-port-list">removePortList</code> (port)
Removes the given port from the port filter list.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to remove from the list.

### Method <code id="remove-addr-list">removeAddrList</code> (addr)
Removes the given address from the address filter list.

<b>Parameters:</b>

- <code><b>addr</b></code> string

  The address you want to remove from the list.

### Method <code id="get-port-list">getPortList</code> () → ports
Allows to get all the ports of the port filter list as array.


<b>Return Values:</b>

- <code><b>ports</b></code> list of integer

  The port array of the filter list.
### Method <code id="get-addr-list">getAddrList</code> () → addresses
Allows to get all the addresses of the address filter list as array.


<b>Return Values:</b>

- <code><b>addresses</b></code> list of string

  The address array of the filter list.
### Method <code id="add-port-list">addPortList</code> (port)
Adds a given port to the port filter list.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to add to the list.

### Method <code id="add-addr-list">addAddrList</code> (addr)


<b>Parameters:</b>

- <code><b>addr</b></code> string

  

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>