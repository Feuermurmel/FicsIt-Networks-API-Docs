# Struct <code>GPUT1Buffer</code>

A structure that can hold a buffer of characters and colors that can be displayed with a gpu
## Instance Members
### Method <code id="get-size">getSize</code> () → width, height
Allows to get the dimensions of the buffer.


<b>Return Values:</b>

- <code><b>width</b></code> float

  The width of this buffer
- <code><b>height</b></code> float

  The height of this buffer
### Method <code id="set-size">setSize</code> (width, height)
Allows to set the dimensions of the buffer.

<b>Parameters:</b>

- <code><b>width</b></code> float

  The width this buffer should now have
- <code><b>height</b></code> float

  The height this buffer now have

### Method <code id="get">get</code> (x, y) → c, foreground, background
Allows to get a single pixel from the buffer at the given position

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x position of the character you want to get
- <code><b>y</b></code> integer

  The y position of the character you want to get

<b>Return Values:</b>

- <code><b>c</b></code> string

  The character at the given position
- <code><b>foreground</b></code> <a href="Color.md">Color</a>

  The foreground color of the pixel at the given position
- <code><b>background</b></code> <a href="Color.md">Color</a>

  The background color of the pixel at the given position
### Method <code id="set">set</code> (x, y, c, foreground, background) → done
Allows to set a single pixel of the buffer at the given position

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x position of the character you want to set
- <code><b>y</b></code> integer

  The y position of the character you want to set
- <code><b>c</b></code> string

  The character the pixel should have
- <code><b>foreground</b></code> <a href="Color.md">Color</a>

  The foreground color the pixel at the given position should have
- <code><b>background</b></code> <a href="Color.md">Color</a>

  The background color the pixel at the given position should have

<b>Return Values:</b>

- <code><b>done</b></code> boolean

  True if the pixel got set successfully
### Method <code id="copy">copy</code> (x, y, buffer, textBlendMode, foregroundBlendMode, backgroundBlendMode)
Copies the given buffer at the given offset of the upper left corner into this buffer.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x offset of the upper left corner of the buffer relative to this buffer
- <code><b>y</b></code> integer

  The y offset of the upper left corner of the buffer relative to this buffer
- <code><b>buffer</b></code> <a href="GPUT1Buffer.md">GPUT1Buffer</a>

  The buffer from wich you want to copy from
- <code><b>textBlendMode</b></code> integer

  The blend mode that is used for the text.
0 = Overwrite this with the content of the given buffer
1 = Overwrite with only characters that are not ' '
2 = Overwrite only were this characters are ' '
3 = Keep this buffer
- <code><b>foregroundBlendMode</b></code> integer

  The blend mode that is used for the foreground color.
0 = Overwrite with the given color
1 = Normal alpha composition
2 = Multiply
3 = Divide
4 = Addition
5 = Subtraction
6 = Difference
7 = Darken Only
8 = Lighten Only
9 = None
- <code><b>backgroundBlendMode</b></code> integer

  The blend mode that is used for the background color.
0 = Overwrite with the given color
1 = Normal alpha composition
2 = Multiply
3 = Divide
4 = Addition
5 = Subtraction
6 = Difference
7 = Darken Only
8 = Lighten Only
9 = None

### Method <code id="set-text">setText</code> (x, y, text, foreground, background)
Allows to write the given text onto the buffer and with the given offset.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The X Position at which the text should begin to get written.
- <code><b>y</b></code> integer

  The Y Position at which the text should begin to get written.
- <code><b>text</b></code> string

  The text that should get written.
- <code><b>foreground</b></code> <a href="Color.md">Color</a>

  The foreground color which will be used to write the text.
- <code><b>background</b></code> <a href="Color.md">Color</a>

  The background color which will be used to write the text.

### Method <code id="fill">fill</code> (x, y, width, height, character, foreground, background)
Draws the given character at all given positions in the given rectangle on-to the hidden screen buffer.

<b>Parameters:</b>

- <code><b>x</b></code> integer

  The x coordinate at which the rectangle should get drawn. (upper-left corner)
- <code><b>y</b></code> integer

  The y coordinate at which the rectangle should get drawn. (upper-left corner)
- <code><b>width</b></code> integer

  The width of the rectangle.
- <code><b>height</b></code> integer

  The height of the rectangle.
- <code><b>character</b></code> string

  A string with a single character that will be used for each pixel in the range you want to fill.
- <code><b>foreground</b></code> <a href="Color.md">Color</a>

  The foreground color which will be used to fill the rectangle.
- <code><b>background</b></code> <a href="Color.md">Color</a>

  The background color which will be used to fill the rectangle.

### Method <code id="set-raw">setRaw</code> (characters, foreground, background) → success
Allows to set the internal data of the buffer more directly.

<b>Parameters:</b>

- <code><b>characters</b></code> string

  The characters you want to draw with a length of exactly width*height.
- <code><b>foreground</b></code> list of float

  The values of the foreground color slots for each character were a group of four values give one color. so the length has to be exactly width*height*4.
- <code><b>background</b></code> list of float

  The values of the background color slots for each character were a group of four values give one color. so the length has to be exactly width*height*4.

<b>Return Values:</b>

- <code><b>success</b></code> boolean

  True if the raw data was successfully written
### Method <code id="clone">clone</code> () → buffer
Clones this buffer into a new struct


<b>Return Values:</b>

- <code><b>buffer</b></code> <a href="GPUT1Buffer.md">GPUT1Buffer</a>

  The clone of this buffer