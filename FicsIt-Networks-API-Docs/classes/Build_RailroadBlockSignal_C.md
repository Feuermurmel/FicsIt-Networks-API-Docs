# Class <code>Build_RailroadBlockSignal_C</code>

Superclasses: <a href="RailroadSignal.md">RailroadSignal</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Train Signals are used to direct the movement of Trains to avoid collisions and bottlenecks.

Block Signals can be placed on Railways to create 'Blocks' between each other. When a Train is occupying such a Block, other Trains will be unable to enter it.

Caution: Signals are directional! Trains are unable to move against this direction, so be sure to set up Signals in both directions for bi-directional Railways.
## Instance Members
<b>Inherited Members:</b>
- RailroadSignal: <a href="RailroadSignal.md#user-content--aspect-changed">AspectChanged</a>, <a href="RailroadSignal.md#user-content-aspect">aspect</a>, <a href="RailroadSignal.md#user-content-block-validation">blockValidation</a>, <a href="RailroadSignal.md#user-content-get-observed-block">getObservedBlock()</a>, <a href="RailroadSignal.md#user-content-has-observed-block">hasObservedBlock</a>, <a href="RailroadSignal.md#user-content-is-bi-directional">isBiDirectional</a>, <a href="RailroadSignal.md#user-content-is-path-signal">isPathSignal</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>