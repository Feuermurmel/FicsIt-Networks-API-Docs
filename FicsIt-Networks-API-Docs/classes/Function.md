# Class <code>Function</code>

Superclasses: <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

A reflection object representing a function.
## Instance Members
<b>Inherited Members:</b>
- ReflectionBase: <a href="ReflectionBase.md#user-content-description">description</a>, <a href="ReflectionBase.md#user-content-display-name">displayName</a>, <a href="ReflectionBase.md#user-content-name">name</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="flags">flags</code> integer

  The function bit flag register defining some behaviour of it.

Bits and their meaning (least significant bit first):
Is this function has a variable amount of input parameters.
Can this function get called in synchronous runtime.
Can this function can get called in parallel runtime.
Can this function get called in asynchronous runtime.
Is this function a member function.
The function is a class function.
The function is a static function.
The function has a variable amount of return values.
### Method <code id="get-parameters">getParameters</code> () → parameters
Returns all the parameters of this function.


<b>Return Values:</b>

- <code><b>parameters</b></code> list of <a href="Property.md">Property</a>

  The parameters this function.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>