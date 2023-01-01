# Class <code>RailroadVehicleMovement</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

This actor component contains all the information about the movement of a railroad vehicle.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#owner">owner</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>orientation</b></code> float

  The orientation of the vehicle
- <code><b>mass</b></code> float

  The current mass of the vehicle.
- <code><b>tareMass</b></code> float

  The tare mass of the vehicle.
- <code><b>payloadMass</b></code> float

  The mass of the payload of the vehicle.
- <code><b>speed</b></code> float

  The current forward speed of the vehicle.
- <code><b>relativeSpeed</b></code> float

  The current relative forward speed to the ground.
- <code><b>maxSpeed</b></code> float

  The maximum forward speed the vehicle can reach.
- <code><b>gravitationalForce</b></code> float

  The current gravitational force acting on the vehicle.
- <code><b>tractiveForce</b></code> float

  The current tractive force acting on the vehicle.
- <code><b>resistiveForce</b></code> float

  The resistive force currently acting on the vehicle.
- <code><b>gradientForce</b></code> float

  The gradient force currently acting on the vehicle.
- <code><b>brakingForce</b></code> float

  The braking force currently acting on the vehicle.
- <code><b>airBrakingForce</b></code> float

  The air braking force currently acting on the vehicle.
- <code><b>dynamicBrakingForce</b></code> float

  The dynamic braking force currently acting on the vehicle.
- <code><b>maxTractiveEffort</b></code> float

  The maximum tractive effort of this vehicle.
- <code><b>maxDynamicBrakingEffort</b></code> float

  The maximum dynamic braking effort of this vehicle.
- <code><b>maxAirBrakingEffort</b></code> float

  The maximum air braking effort of this vehicle.
- <code><b>trackGrade</b></code> float

  The current track grade of this vehicle.
- <code><b>trackCurvature</b></code> float

  The current track curvature of this vehicle.
- <code><b>wheelsetAngle</b></code> float

  The wheelset angle of this vehicle.
- <code><b>rollingResistance</b></code> float

  The current rolling resistance of this vehicle.
- <code><b>curvatureResistance</b></code> float

  The current curvature resistance of this vehicle.
- <code><b>airResistance</b></code> float

  The current air resistance of this vehicle.
- <code><b>gradientResistance</b></code> float

  The current gradient resistance of this vehicle.
- <code><b>wheelRotation</b></code> float

  The current wheel rotation of this vehicle.
- <code><b>numWheelsets</b></code> integer

  The number of wheelsets this vehicle has.
- <code><b>isMoving</b></code> boolean

  True if this vehicle is currently moving.
### Method <code>getVehicle</code> () → vehicle
Returns the vehicle this movement component holds the movement information of.


<b>Return Values:</b>

- <code><b>vehicle</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The vehicle this movement component holds the movement information of.
### Method <code>getWheelsetRotation</code> (wheelset) → x, y, z
Returns the current rotation of the given wheelset.

<b>Parameters:</b>

- <code><b>wheelset</b></code> integer

  The index of the wheelset you want to get the rotation of.

<b>Return Values:</b>

- <code><b>x</b></code> float

  The wheelset's rotation X component.
- <code><b>y</b></code> float

  The wheelset's rotation Y component.
- <code><b>z</b></code> float

  The wheelset's rotation Z component.
### Method <code>getWheelsetOffset</code> (wheelset) → offset
Returns the offset of the wheelset with the given index from the start of the vehicle.

<b>Parameters:</b>

- <code><b>wheelset</b></code> integer

  The index of the wheelset you want to get the offset of.

<b>Return Values:</b>

- <code><b>offset</b></code> float

  The offset of the wheelset.
### Method <code>getCouplerRotationAndExtension</code> (coupler) → x, y, z, extension
Returns the normal vector and the extension of the coupler with the given index.

<b>Parameters:</b>

- <code><b>coupler</b></code> integer

  The index of which you want to get the normal and extension of.

<b>Return Values:</b>

- <code><b>x</b></code> float

  The X component of the coupler normal.
- <code><b>y</b></code> float

  The Y component of the coupler normal.
- <code><b>z</b></code> float

  The Z component of the coupler normal.
- <code><b>extension</b></code> float

  The extension of the coupler.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>