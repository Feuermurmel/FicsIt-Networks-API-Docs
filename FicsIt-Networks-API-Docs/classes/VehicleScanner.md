# Class <code>VehicleScanner</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="VehicleScanner_C.md">VehicleScanner_C</a>


## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="set-color">setColor</code> (r, g, b, e)
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

### Method <code id="get-last-vehicle">getLastVehicle</code> () → vehicle
Returns the last vehicle that entered the scanner.


<b>Return Values:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that entered the scanner. null if it has already left the scanner.
### Method <code id="get-color">getColor</code> () → r, g, b, e
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
### Signal <code id="-on-vehicle-exit">OnVehicleExit</code> → vehicle
Triggers when a vehicle leaves the scanner.

<b>Parameters:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that left the scanner.
### Signal <code id="-on-vehicle-enter">OnVehicleEnter</code> → vehicle
Triggers when a vehicle enters the scanner.

<b>Parameters:</b>

- <code><b>vehicle</b></code> <a href="Vehicle.md">Vehicle</a>

  The vehicle that entered the scanner.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>