# Class <code>RailroadSignal</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

A train signal to control trains on a track.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Fields
- <code><b>isPathSignal</b></code> boolean

  True if this signal is a path-signal.
- <code><b>isBiDirectional</b></code> boolean

  True if this signal is bi-directional. (trains can pass into both directions)
- <code><b>hasObservedBlock</b></code> boolean

  True if this signal is currently observing at least one block.
- <code><b>blockValidation</b></code> integer

  Any error states of the block.
0 = Unknown
1 = No Error
2 = No Exit Signal
3 = Contains Loop
4 = Contains Mixed Entry Signals
- <code><b>aspect</b></code> integer

  The aspect of the signal. The aspect shows if a train is allowed to pass (clear) or not and if it should dock.
0 = Unknown
1 = The track is clear and the train is allowed to pass.
2 = The next track is Occupied and the train should stop
3 = The train should dock.
### Method <code>getObservedBlock() -> block</code>
Returns the track block this signals observes.

<b>Return Values:</b>

- <code><b>block</b></code> <a href="../structs/RailroadSignalBlock.md">RailroadSignalBlock</a>

  The railroad signal block this signal is observing.
### Signal <code>AspectChanged -> aspect</code>
Triggers when the aspect of this signal changes.

<b>Parameters:</b>

- <code><b>aspect</b></code> integer

  The new aspect of the signal (see 'Get Aspect' for more information)
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>