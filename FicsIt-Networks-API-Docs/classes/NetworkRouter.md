# Class <code>NetworkRouter</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isWhitelist</b></code> boolean

  
- <code><b>isAddrWhitelist</b></code> boolean

  True if the address filter list is used as whitelist.
### Method <code>setPortList</code> () → ports
Overrides the port filter list with the given array.


<b>Return Values:</b>

- <code><b>ports</b></code> list of integer

  The port array you want to override the filter list with.
### Method <code>setAddrList</code> () → addresses
Overrides the address filter list with the given array.


<b>Return Values:</b>

- <code><b>addresses</b></code> list of string

  The address array you want to override the filter list with.
### Method <code>removePortList</code> (port) → 
Removes the given port from the port filter list.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to remove from the list.

### Method <code>removeAddrList</code> (addr) → 
Removes the given address from the address filter list.

<b>Parameters:</b>

- <code><b>addr</b></code> string

  The address you want to remove from the list.

### Method <code>getPortList</code> () → ports
Allows to get all the ports of the port filter list as array.


<b>Return Values:</b>

- <code><b>ports</b></code> list of integer

  The port array of the filter list.
### Method <code>getAddrList</code> () → addresses
Allows to get all the addresses of the address filter list as array.


<b>Return Values:</b>

- <code><b>addresses</b></code> list of string

  The address array of the filter list.
### Method <code>addPortList</code> (port) → 
Adds a given port to the port filter list.

<b>Parameters:</b>

- <code><b>port</b></code> integer

  The port you want to add to the list.

### Method <code>addAddrList</code> (addr) → 


<b>Parameters:</b>

- <code><b>addr</b></code> string

  

## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>