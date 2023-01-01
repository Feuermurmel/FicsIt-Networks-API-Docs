# Struct <code>PrefabSignData</code>

This structure stores all data that defines what a sign displays.
## Instance Members
### Fields
- <code><b>layout</b></code> <a href="../classes/Object.md">Object</a>

  The object that actually displays the layout
- <code><b>foreground</b></code> <a href="Color.md">Color</a>

  The foreground Color.
- <code><b>background</b></code> <a href="Color.md">Color</a>

  The background Color.
- <code><b>auxiliary</b></code> <a href="Color.md">Color</a>

  The auxiliary Color.
- <code><b>signType</b></code> <a href="../classes/SignType.md">SignType</a>

  The type of sign this prefab fits to.
### Method <code>getTextElements</code> () → textElements, textElementValues
Returns all text elements and their values.


<b>Return Values:</b>

- <code><b>textElements</b></code> list of string

  The element names for all text elements.
- <code><b>textElementValues</b></code> list of string

  The values for all text elements.
### Method <code>getIconElements</code> () → iconElements, iconElementValues
Returns all icon elements and their values.


<b>Return Values:</b>

- <code><b>iconElements</b></code> list of string

  The element names for all icon elements.
- <code><b>iconElementValues</b></code> list of integer

  The values for all icon elements.
### Method <code>setTextElements</code> (textElements, textElementValues) → 
Sets all text elements and their values.

<b>Parameters:</b>

- <code><b>textElements</b></code> list of string

  The element names for all text elements.
- <code><b>textElementValues</b></code> list of string

  The values for all text elements.

### Method <code>setIconElements</code> (iconElements, iconElementValues) → 
Sets all icon elements and their values.

<b>Parameters:</b>

- <code><b>iconElements</b></code> list of string

  The element names for all icon elements.
- <code><b>iconElementValues</b></code> list of integer

  The values for all icon elements.

### Method <code>setTextElement</code> (elementName, value) → 
Sets a text element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the text element
- <code><b>value</b></code> string

  The value of the text element

### Method <code>setIconElement</code> (elementName, value) → 
Sets a icon element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the icon element
- <code><b>value</b></code> integer

  The value of the icon element

### Method <code>getTextElement</code> (elementName) → value
Gets a text element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the text element

<b>Return Values:</b>

- <code><b>value</b></code> integer

  The value of the text element
### Method <code>getIconElement</code> (elementName) → value
Gets a icon element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the icon element

<b>Return Values:</b>

- <code><b>value</b></code> integer

  The value of the icon element