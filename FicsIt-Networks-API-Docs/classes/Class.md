# Class <code>Class</code>

Superclasses: <a href="Struct.md">Struct</a> < <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

Object that contains all information about a type.
## Instance Members
<b>Inherited Members:</b>
- Struct: <a href="Struct.md#getAllFunctions">getAllFunctions()</a>, <a href="Struct.md#getAllProperties">getAllProperties()</a>, <a href="Struct.md#getFunctions">getFunctions()</a>, <a href="Struct.md#getParent">getParent()</a>, <a href="Struct.md#getProperties">getProperties()</a>, <a href="Struct.md#isChildOf">isChildOf()</a>
- ReflectionBase: <a href="ReflectionBase.md#description">description</a>, <a href="ReflectionBase.md#displayName">displayName</a>, <a href="ReflectionBase.md#name">name</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getSignals</code> () → signals
Returns all the signals of this type.

<b>Return Values:</b>

- <code><b>signals</b></code> list of <a href="Signal.md">Signal</a>

  The signals this specific type implements (excluding properties from parent types).
### Method <code>getAllSignals</code> () → signals
Returns all the signals of this and its parent types.

<b>Return Values:</b>

- <code><b>signals</b></code> list of <a href="Signal.md">Signal</a>

  The signals this type and all it parents implement.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>