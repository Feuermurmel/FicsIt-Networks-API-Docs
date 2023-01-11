# Class <code>Class</code>

Superclasses: <a href="Struct.md">Struct</a> < <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

Object that contains all information about a type.
## Instance Members
<b>Inherited Members:</b>
- Struct: <a href="Struct.md#user-content-get-all-functions">getAllFunctions()</a>, <a href="Struct.md#user-content-get-all-properties">getAllProperties()</a>, <a href="Struct.md#user-content-get-functions">getFunctions()</a>, <a href="Struct.md#user-content-get-parent">getParent()</a>, <a href="Struct.md#user-content-get-properties">getProperties()</a>, <a href="Struct.md#user-content-is-child-of">isChildOf()</a>
- ReflectionBase: <a href="ReflectionBase.md#user-content-description">description</a>, <a href="ReflectionBase.md#user-content-display-name">displayName</a>, <a href="ReflectionBase.md#user-content-name">name</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="get-signals">getSignals</code> () → signals
Returns all the signals of this type.


<b>Return Values:</b>

- <code><b>signals</b></code> list of <a href="Signal.md">Signal</a>

  The signals this specific type implements (excluding properties from parent types).
### Method <code id="get-all-signals">getAllSignals</code> () → signals
Returns all the signals of this and its parent types.


<b>Return Values:</b>

- <code><b>signals</b></code> list of <a href="Signal.md">Signal</a>

  The signals this type and all it parents implement.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>