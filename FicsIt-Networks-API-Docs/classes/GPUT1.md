# Class <code>GPUT1</code>

Superclasses: <a href="FINComputerGPU.md">FINComputerGPU</a> < <a href="FINComputerModule.md">FINComputerModule</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- FINComputerGPU: <a href="FINComputerGPU.md#ScreenBound">ScreenBound</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>setText</code> (x, y, str) → 
Draws the given text at the given position to the hidden screen buffer.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x coordinate at which the text should get drawn.
- <code><b>y</b></code> integer

  The y coordinate at which the text should get drawn.
- <code><b>str</b></code> string

  The text you want to draw on-to the buffer.

### Method <code>setSize</code> (w, h) → 
Changes the size of the text-grid (and buffer).

<b>Parameters:</b>

- <code><b>w</b></code> integer

  The width of the text-gird.
- <code><b>h</b></code> integer

  The height of the text-grid.

### Method <code>setForeground</code> (r, g, b, a) → 
Changes the foreground color that is used for the next draw calls.

<b>Parameters:</b>

- <code><b>r</b></code> float

  The red portion of the foreground color. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green portion of the foreground color. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue portion of the foreground color. (0.0 - 1.0)
- <code><b>a</b></code> float

  The opacity of the foreground color. (0.0 - 1.0)

### Method <code>setBuffer</code> (buffer) → 
Allows to change the back buffer of the GPU to the given buffer.

<b>Parameters:</b>

- <code><b>buffer</b></code> <a href="../structs/GPUT1Buffer.md">GPUT1Buffer</a>

  The Buffer you want to now use as back buffer.

### Method <code>setBackground</code> (r, g, b, a) → 
Changes the background color that is used for the next draw calls.

<b>Parameters:</b>

- <code><b>r</b></code> float

  The red portion of the background color. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green portion of the background color. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue portion of the background color. (0.0 - 1.0)
- <code><b>a</b></code> float

  The opacity of the background color. (0.0 - 1.0)

### Method <code>getSize</code> () → w, h
Returns the size of the text-grid (and buffer).


<b>Return Values:</b>

- <code><b>w</b></code> integer

  The width of the text-gird.
- <code><b>h</b></code> integer

  The height of the text-grid.
### Method <code>getScreen</code> () → screen
Returns the currently bound screen.


<b>Return Values:</b>

- <code><b>screen</b></code> <a href="Object.md">Object</a>

  The currently bound screen.
### Method <code>getBuffer</code> () → buffer
Returns the back buffer as struct to be able to use advanced buffer handling functions. (struct is a copy)


<b>Return Values:</b>

- <code><b>buffer</b></code> <a href="../structs/GPUT1Buffer.md">GPUT1Buffer</a>

  The Buffer that is currently the back buffer.
### Method <code>flush</code> () → 
Flushes the hidden screen buffer to the visible screen buffer and so makes the draw calls visible.


### Method <code>fill</code> (x, y, dx, dy, str) → 
Draws the given character at all given positions in the given rectangle on-to the hidden screen buffer.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x coordinate at which the rectangle should get drawn. (upper-left corner)
- <code><b>y</b></code> integer

  The y coordinate at which the rectangle should get drawn. (upper-left corner)
- <code><b>dx</b></code> integer

  The width of the rectangle.
- <code><b>dy</b></code> integer

  The height of the rectangle.
- <code><b>str</b></code> string

  The character you want to use for the rectangle. (first char in the given string)

### Method <code>bindScreen</code> (newScreen) → 
Binds this GPU to the given screen. Unbinds the already bound screen.

<b>Parameters:</b>

- <code><b>newScreen</b></code> unknown

  The screen you want to bind this GPU to. Null if you want to unbind the screen.

### Signal <code>ScreenSizeChanged</code> → oldW, oldH
Triggers when the size of the text grid changed.

<b>Parameters:</b>

- <code><b>oldW</b></code> integer

  The old width of the screen.
- <code><b>oldH</b></code> integer

  The old height of the screen.
### Signal <code>OnMouseUp</code> → x, y, btn
Triggers when a mouse button got released.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x position of the cursor.
- <code><b>y</b></code> integer

  The y position of the cursor.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the released button event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
### Signal <code>OnMouseMove</code> → x, y, btn
Triggers when the mouse cursor moves on the screen.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x position of the cursor.
- <code><b>y</b></code> integer

  The y position of the cursor.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the move event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
### Signal <code>OnMouseDown</code> → x, y, btn
Triggers when a mouse button got pressed.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x position of the cursor.
- <code><b>y</b></code> integer

  The y position of the cursor.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the pressed button event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
### Signal <code>OnKeyUp</code> → c, code, btn
Triggers when a key got released.

<b>Parameters:</b>

- <code><b>c</b></code> integer

  The ASCII number of the character typed in.
- <code><b>code</b></code> integer

  The number code of the pressed key.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the key release event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
### Signal <code>OnKeyDown</code> → c, code, btn
Triggers when a key got pressed.

<b>Parameters:</b>

- <code><b>c</b></code> integer

  The ASCII number of the character typed in.
- <code><b>code</b></code> integer

  The number code of the pressed key.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the key press event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
### Signal <code>OnKeyChar</code> → c, btn
Triggers when a character key got 'clicked' and essentially a character got typed in, useful for text input.

<b>Parameters:</b>

- <code><b>c</b></code> string

  The character that got typed in as string.
- <code><b>btn</b></code> integer

  The Button-Bit-Field providing information about the key release event.
Bits:
1th left mouse pressed
2th right mouse button pressed
3th ctrl key pressed
4th shift key pressed
5th alt key pressed
6th cmd key pressed
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>