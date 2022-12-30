# Class <code>Struct</code>

Superclasses: <a href="ReflectionBase.md">ReflectionBase</a> < <a href="Object.md">Object</a>

Reflection Object that holds information about structures.
## Instance Members
<b>Inherited Members:</b>
- ReflectionBase: <a href="ReflectionBase.md#description">description</a>, <a href="ReflectionBase.md#displayName">displayName</a>, <a href="ReflectionBase.md#name">name</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>getParent</code> () → parent
Returns the parent type of this type.

<b>Return Values:</b>

- <code><b>parent</b></code> <a href="Class.md">Class</a>

  The parent type of this type.
### Method <code>getProperties</code> () → properties
Returns all the properties of this type.

<b>Return Values:</b>

- <code><b>properties</b></code> list of <a href="Property.md">Property</a>

  The properties this specific type implements (excluding properties from parent types).
### Method <code>getAllProperties</code> () → properties
Returns all the properties of this and parent types.

<b>Return Values:</b>

- <code><b>properties</b></code> list of <a href="Property.md">Property</a>

  The properties this type implements including properties from parent types.
### Method <code>getFunctions</code> () → functions
Returns all the functions of this type.

<b>Return Values:</b>

- <code><b>functions</b></code> list of <a href="Function.md">Function</a>

  The functions this specific type implements (excluding properties from parent types).
### Method <code>getAllFunctions</code> () → functions
Returns all the functions of this and parent types.

<b>Return Values:</b>

- <code><b>functions</b></code> list of <a href="Property.md">Property</a>

  The functions this type implements including functions from parent types.
### Method <code>isChildOf</code> (parent) → isChild
Allows to check if this struct is a child struct of the given struct or the given struct it self.

<b>Parameters:</b>

- <code><b>parent</b></code> <a href="Struct.md">Struct</a>

  The parent struct you want to check if this struct is a child of.
<b>Return Values:</b>

- <code><b>isChild</b></code> boolean

  True if this struct is a child of parent.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>