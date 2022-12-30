# Class <code>Function</code>

Superclasses: <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

A reflection object representing a function.
## Instance Members
<b>Inherited Members:</b>
- ReflectionBase: <a href="ReflectionBase.md#description">description</a>, <a href="ReflectionBase.md#displayName">displayName</a>, <a href="ReflectionBase.md#name">name</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>flags</b></code> integer

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
### Method <code>getParameters</code> () → parameters
Returns all the parameters of this function.

<b>Return Values:</b>

- <code><b>parameters</b></code> list of <a href="Property.md">Property</a>

  The parameters this function.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>