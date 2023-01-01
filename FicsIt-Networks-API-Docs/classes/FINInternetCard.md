# Class <code>FINInternetCard</code>

Superclasses: <a href="FINComputerModule.md">FINComputerModule</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>request</code> (url, method, data, args) → ReturnValue
Does an HTTP-Request. If a payload is given, the Content-Type header has to be set. All additional parameters have to be strings and in pairs of two for defining the http headers and values.

<b>Parameters:</b>

- <code><b>url</b></code> string

  The URL for which you want to make an HTTP Request.
- <code><b>method</b></code> string

  The http request method/verb you want to make the request. f.e. 'GET', 'POST'
- <code><b>data</b></code> string

  The http request payload you want to sent.
- <code><b>args</b></code> unknown

  

<b>Return Values:</b>

- <code><b>ReturnValue</b></code> <a href="../structs/Future.md">Future</a>

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>