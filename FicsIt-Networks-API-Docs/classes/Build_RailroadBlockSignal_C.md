# Class <code>Build_RailroadBlockSignal_C</code>

Superclasses: <a href="RailroadSignal.md">RailroadSignal</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Train Signals are used to direct the movement of Trains to avoid collisions and bottlenecks.

Block Signals can be placed on Railways to create 'Blocks' between each other. When a Train is occupying such a Block, other Trains will be unable to enter it.

Caution: Signals are directional! Trains are unable to move against this direction, so be sure to set up Signals in both directions for bi-directional Railways.
## Instance Members
<b>Inherited Members:</b>
- RailroadSignal: <a href="RailroadSignal.md#AspectChanged">AspectChanged</a>, <a href="RailroadSignal.md#aspect">aspect</a>, <a href="RailroadSignal.md#blockValidation">blockValidation</a>, <a href="RailroadSignal.md#getObservedBlock">getObservedBlock()</a>, <a href="RailroadSignal.md#hasObservedBlock">hasObservedBlock</a>, <a href="RailroadSignal.md#isBiDirectional">isBiDirectional</a>, <a href="RailroadSignal.md#isPathSignal">isPathSignal</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>