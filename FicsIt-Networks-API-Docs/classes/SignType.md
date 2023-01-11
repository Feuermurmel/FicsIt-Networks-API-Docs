# Class <code>SignType</code>

Superclasses: <a href="Object.md">Object</a>

Describes the type of a sign.
## Instance Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>
### Fields
- <code id="s-dimensions">dimensions</code> <a href="../structs/Vector2D.md">Vector2D</a>

  The canvas dimensions of this sign.
### Method <code id="s-get-colors">getColors</code> () → foreground, background, auxiliary
Returns the default foreground/background/auxiliary colors of this sign type.


<b>Return Values:</b>

- <code><b>foreground</b></code> <a href="../structs/Color.md">Color</a>

  The foreground color
- <code><b>background</b></code> <a href="../structs/Color.md">Color</a>

  The background color
- <code><b>auxiliary</b></code> <a href="../structs/Color.md">Color</a>

  The auxiliary color
### Method <code id="s-get-prefabs">getPrefabs</code> () → prefabs
Returns a list of all sign prefabs this sign can use.


<b>Return Values:</b>

- <code><b>prefabs</b></code> list of <a href="SignPrefab.md">SignPrefab</a>

  The sign prefabs this sign can use
### Method <code id="s-get-text-elements">getTextElements</code> () → textElementsDefaultValues
Returns a list of element names and their default text values.


<b>Return Values:</b>

- <code><b>textElementsDefaultValues</b></code> list of string

  A list of default values for the text elements of this type.
### Method <code id="s-get-icon-elements">getIconElements</code> () → iconElementsDefaultValues
Returns a list of element names and their default icon values.


<b>Return Values:</b>

- <code><b>iconElementsDefaultValues</b></code> list of <a href="Object.md">Object</a>

  A list of default values for the icon elements of this type.