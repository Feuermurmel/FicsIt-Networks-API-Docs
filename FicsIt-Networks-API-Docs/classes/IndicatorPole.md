# Class <code>IndicatorPole</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>setColor</code> (r, g, b, e) → 
Allows to change the color and light intensity of the indicator lamp.

<b>Parameters:</b>

- <code><b>r</b></code> float

  The red part of the color in which the light glows. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green part of the color in which the light glows. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue part of the color in which the light glows. (0.0 - 1.0)
- <code><b>e</b></code> float

  The light intensity of the pole. (0.0 - 5.0)

### Method <code>getTopPole</code> () → topPole
Allows to get the pole placed on top of this pole.


<b>Return Values:</b>

- <code><b>topPole</b></code> <a href="IndicatorPole.md">IndicatorPole</a>

  The pole placed on top of this pole.
### Method <code>getColor</code> () → r, g, b, e
Allows to get the color and light intensity of the indicator lamp.


<b>Return Values:</b>

- <code><b>r</b></code> float

  The red part of the color in which the light glows. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green part of the color in which the light glows. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue part of the color in which the light glows. (0.0 - 1.0)
- <code><b>e</b></code> float

  The light intensity of the pole. (0.0 - 5.0)
### Method <code>getBottomPole</code> () → ReturnValue



<b>Return Values:</b>

- <code><b>ReturnValue</b></code> <a href="IndicatorPole.md">IndicatorPole</a>

  
### Signal <code>ColorChanged</code> → r, g, b, e
Triggers when the color of the indicator pole changes.

<b>Parameters:</b>

- <code><b>r</b></code> float

  The red part of the color in which the light glows. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green part of the color in which the light glows. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue part of the color in which the light glows. (0.0 - 1.0)
- <code><b>e</b></code> float

  The light intensity of the pole. (0.0 - 5.0)
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>