# Class <code>Property</code>

Superclasses: <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

A Reflection object that holds information about properties and parameters.
## Instance Members
<b>Inherited Members:</b>
- ReflectionBase: <a href="ReflectionBase.md#user-content-description">description</a>, <a href="ReflectionBase.md#user-content-display-name">displayName</a>, <a href="ReflectionBase.md#user-content-name">name</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="data-type">dataType</code> integer

  The data type of this property.
0: nil, 1: bool, 2: int, 3: float, 4: str, 5: object, 6: class, 7: trace, 8: struct, 9: array, 10: anything
- <code id="flags">flags</code> integer

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
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>