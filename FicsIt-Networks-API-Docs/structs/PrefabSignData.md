# Struct <code>PrefabSignData</code>

This structure stores all data that defines what a sign displays.
## Instance Members
### Fields
- <code id="layout">layout</code> <a href="../classes/Object.md">Object</a>

  The object that actually displayes the layout
- <code id="foreground">foreground</code> <a href="Color.md">Color</a>

  The foreground Color.
- <code id="background">background</code> <a href="Color.md">Color</a>

  The background Color.
- <code id="auxiliary">auxiliary</code> <a href="Color.md">Color</a>

  The auxiliary Color.
- <code id="sign-type">signType</code> <a href="../classes/SignType.md">SignType</a>

  The type of sign this prefab fits to.
### Method <code id="get-text-elements">getTextElements</code> () → textElements, textElementValues
Returns all text elements and their values.


<b>Return Values:</b>

- <code><b>textElements</b></code> list of string

  The element names for all text elements.
- <code><b>textElementValues</b></code> list of string

  The values for all text elements.
### Method <code id="get-icon-elements">getIconElements</code> () → iconElements, iconElementValues
Returns all icon elements and their values.


<b>Return Values:</b>

- <code><b>iconElements</b></code> list of string

  The element names for all icon elements.
- <code><b>iconElementValues</b></code> list of integer

  The values for all icon elements.
### Method <code id="set-text-elements">setTextElements</code> (textElements, textElementValues)
Sets all text elements and their values.

<b>Parameters:</b>

- <code><b>textElements</b></code> list of string

  The element names for all text elements.
- <code><b>textElementValues</b></code> list of string

  The values for all text elements.

### Method <code id="set-icon-elements">setIconElements</code> (iconElements, iconElementValues)
Sets all icon elements and their values.

<b>Parameters:</b>

- <code><b>iconElements</b></code> list of string

  The element names for all icon elements.
- <code><b>iconElementValues</b></code> list of integer

  The values for all icon elements.

### Method <code id="set-text-element">setTextElement</code> (elementName, value)
Sets a text element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the text element
- <code><b>value</b></code> string

  The value of the text element

### Method <code id="set-icon-element">setIconElement</code> (elementName, value)
Sets a icon element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the icon element
- <code><b>value</b></code> integer

  The value of the icon element

### Method <code id="get-text-element">getTextElement</code> (elementName) → value
Gets a text element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the text element

<b>Return Values:</b>

- <code><b>value</b></code> integer

  The value of the text element
### Method <code id="get-icon-element">getIconElement</code> (elementName) → value
Gets a icon element with the given element name.

<b>Parameters:</b>

- <code><b>elementName</b></code> string

  The name of the icon element

<b>Return Values:</b>

- <code><b>value</b></code> integer

  The value of the icon element