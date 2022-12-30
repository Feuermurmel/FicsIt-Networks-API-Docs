# Class <code>Property</code>

Superclasses: <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

A Reflection object that holds information about properties and parameters.
## Instance Members
<b>Inherited Members:</b>
- ReflectionBase: <a href="ReflectionBase.md#description">description</a>, <a href="ReflectionBase.md#displayName">displayName</a>, <a href="ReflectionBase.md#name">name</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>dataType</b></code> integer

  The data type of this property.
0: nil, 1: bool, 2: int, 3: float, 4: str, 5: object, 6: class, 7: trace, 8: struct, 9: array, 10: anything
- <code><b>flags</b></code> integer

  The property bit flag register defining some behaviour of it.

Bits and their meaning (least significant bit first):
Is this property a member attribute.
Is this property read only.
Is this property a parameter.
Is this property a output parameter.
Is this property a return value.
Can this property get accessed in synchronous runtime.
Can this property can get accessed in parallel runtime.
Can this property get accessed in asynchronous runtime.
This property is a class attribute.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>