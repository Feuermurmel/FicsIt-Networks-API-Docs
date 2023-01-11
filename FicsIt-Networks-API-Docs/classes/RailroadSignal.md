# Class <code>RailroadSignal</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Build_RailroadBlockSignal_C.md">Build_RailroadBlockSignal_C</a>, <a href="Build_RailroadPathSignal_C.md">Build_RailroadPathSignal_C</a>

A train signal to control trains on a track.
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Fields
- <code id="is-path-signal">isPathSignal</code> boolean

  True if this signal is a path-signal.
- <code id="is-bi-directional">isBiDirectional</code> boolean

  True if this signal is bi-directional. (trains can pass into both directions)
- <code id="has-observed-block">hasObservedBlock</code> boolean

  True if this signal is currently observing at least one block.
- <code id="block-validation">blockValidation</code> integer

  Any error states of the block.
0 = Unknown
1 = No Error
2 = No Exit Signal
3 = Contains Loop
4 = Contains Mixed Entry Signals
- <code id="aspect">aspect</code> integer

  The aspect of the signal. The aspect shows if a train is allowed to pass (clear) or not and if it should dock.
0 = Unknown
1 = The track is clear and the train is allowed to pass.
2 = The next track is Occupied and the train should stop
3 = The train should dock.
### Method <code id="get-observed-block">getObservedBlock</code> () → block
Returns the track block this signals observes.


<b>Return Values:</b>

- <code><b>block</b></code> <a href="../structs/RailroadSignalBlock.md">RailroadSignalBlock</a>

  The railroad signal block this signal is observing.
### Signal <code id="-aspect-changed">AspectChanged</code> → aspect
Triggers when the aspect of this signal changes.

<b>Parameters:</b>

- <code><b>aspect</b></code> integer

  The new aspect of the signal (see 'Get Aspect' for more information)
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>