# Class <code>VehicleScanner</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>setColor(r, g, b, e) -> </code>
Allows to change the color and light intensity of the scanner.

<b>Parameters:</b>

- <code><b>r</b></code> float

  The red part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>e</b></code> float

  The light intensity of the scanner. (0.0 - 5.0)
### Method <code>getLastVehicle() -> vehicle</code>
Returns the last vehicle that entered the scanner.

<b>Return Values:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that entered the scanner. null if it has already left the scanner.
### Method <code>getColor() -> r, g, b, e</code>
Allows to get the color and light intensity of the scanner.

<b>Return Values:</b>

- <code><b>r</b></code> float

  The red part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>g</b></code> float

  The green part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>b</b></code> float

  The blue part of the color in which the scanner glows. (0.0 - 1.0)
- <code><b>e</b></code> float

  The light intensity of the scanner. (0.0 - 5.0)
### Signal <code>OnVehicleExit -> vehicle</code>
Triggers when a vehicle leaves the scanner.

<b>Parameters:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that left the scanner.
### Signal <code>OnVehicleEnter -> vehicle</code>
Triggers when a vehicle enters the scanner.

<b>Parameters:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that entered the scanner.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>