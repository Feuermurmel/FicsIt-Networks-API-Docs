# Class <code>SignType</code>

Superclasses: <a href="Object.md">Object</a>

Describes the type of a sign.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>dimensions</b></code> <a href="../structs/Vector2D.md">Vector2D</a>

  The canvas dimensions of this sign.
### Method <code>getColors() -> foreground, background, auxiliary</code>
Returns the default foreground/background/auxiliary colors of this sign type.

<b>Return Values:</b>

- <code><b>foreground</b></code> <a href="../structs/Color.md">Color</a>

  The foreground color
- <code><b>background</b></code> <a href="../structs/Color.md">Color</a>

  The background color
- <code><b>auxiliary</b></code> <a href="../structs/Color.md">Color</a>

  The auxiliary color
### Method <code>getPrefabs() -> prefabs</code>
Returns a list of all sign prefabs this sign can use.

<b>Return Values:</b>

- <code><b>prefabs</b></code> list of <a href="SignPrefab.md">SignPrefab</a>

  The sign prefabs this sign can use
### Method <code>getTextElements() -> textElementsDefaultValues</code>
Returns a list of element names and their default text values.

<b>Return Values:</b>

- <code><b>textElementsDefaultValues</b></code> list of string

  A list of default values for the text elements of this type.
### Method <code>getIconElements() -> iconElementsDefaultValues</code>
Returns a list of element names and their default icon values.

<b>Return Values:</b>

- <code><b>iconElementsDefaultValues</b></code> list of <a href="Object.md">Object</a>

  A list of default values for the icon elements of this type.