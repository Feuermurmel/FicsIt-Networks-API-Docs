# Class <code>RailroadVehicleMovement</code>

Superclasses: <a href="ActorComponent.md">ActorComponent</a> < <a href="Object.md">Object</a>

This actor component contains all the information about the movement of a railroad vehicle.
## Instance Members
<b>Inherited Members:</b>
- ActorComponent: <a href="ActorComponent.md#user-content-owner">owner</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="orientation">orientation</code> float

  The orientation of the vehicle
- <code id="mass">mass</code> float

  The current mass of the vehicle.
- <code id="tare-mass">tareMass</code> float

  The tare mass of the vehicle.
- <code id="payload-mass">payloadMass</code> float

  The mass of the payload of the vehicle.
- <code id="speed">speed</code> float

  The current forward speed of the vehicle.
- <code id="relative-speed">relativeSpeed</code> float

  The current relative forward speed to the ground.
- <code id="max-speed">maxSpeed</code> float

  The maximum forward speed the vehicle can reach.
- <code id="gravitational-force">gravitationalForce</code> float

  The current gravitational force acting on the vehicle.
- <code id="tractive-force">tractiveForce</code> float

  The current tractive force acting on the vehicle.
- <code id="resistive-force">resistiveForce</code> float

  The resistive force currently acting on the vehicle.
- <code id="gradient-force">gradientForce</code> float

  The gradient force currently acting on the vehicle.
- <code id="braking-force">brakingForce</code> float

  The braking force currently acting on the vehicle.
- <code id="air-braking-force">airBrakingForce</code> float

  The air braking force currently acting on the vehicle.
- <code id="dynamic-braking-force">dynamicBrakingForce</code> float

  The dynamic braking force currently acting on the vehicle.
- <code id="max-tractive-effort">maxTractiveEffort</code> float

  The maximum tractive effort of this vehicle.
- <code id="max-dynamic-braking-effort">maxDynamicBrakingEffort</code> float

  The maximum dynamic braking effort of this vehicle.
- <code id="max-air-braking-effort">maxAirBrakingEffort</code> float

  The maximum air braking effort of this vehicle.
- <code id="track-grade">trackGrade</code> float

  The current track grade of this vehicle.
- <code id="track-curvature">trackCurvature</code> float

  The current track curvature of this vehicle.
- <code id="wheelset-angle">wheelsetAngle</code> float

  The wheelset angle of this vehicle.
- <code id="rolling-resistance">rollingResistance</code> float

  The current rolling resistance of this vehicle.
- <code id="curvature-resistance">curvatureResistance</code> float

  The current curvature resistance of this vehicle.
- <code id="air-resistance">airResistance</code> float

  The current air resistance of this vehicle.
- <code id="gradient-resistance">gradientResistance</code> float

  The current gradient resistance of this vehicle.
- <code id="wheel-rotation">wheelRotation</code> float

  The current wheel rotation of this vehicle.
- <code id="num-wheelsets">numWheelsets</code> integer

  The number of wheelsets this vehicle has.
- <code id="is-moving">isMoving</code> boolean

  True if this vehicle is currently moving.
### Method <code id="get-vehicle">getVehicle</code> () → vehicle
Returns the vehicle this movement component holds the movement information of.


<b>Return Values:</b>

- <code><b>vehicle</b></code> <a href="RailroadVehicle.md">RailroadVehicle</a>

  The vehicle this movement component holds the movement information of.
### Method <code id="get-wheelset-rotation">getWheelsetRotation</code> (wheelset) → x, y, z
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
### Method <code id="get-wheelset-offset">getWheelsetOffset</code> (wheelset) → offset
Returns the offset of the wheelset with the given index from the start of the vehicle.

<b>Parameters:</b>

- <code><b>wheelset</b></code> integer

  The index of the wheelset you want to get the offset of.

<b>Return Values:</b>

- <code><b>offset</b></code> float

  The offset of the wheelset.
### Method <code id="get-coupler-rotation-and-extension">getCouplerRotationAndExtension</code> (coupler) → x, y, z, extension
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
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>