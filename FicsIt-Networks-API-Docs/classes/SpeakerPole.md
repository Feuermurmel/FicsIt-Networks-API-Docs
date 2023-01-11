# Class <code>SpeakerPole</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

Direct subclasses: <a href="Speakers_C.md">Speakers_C</a>

This speaker pole allows to play custom sound files, In-Game
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="stop-sound">stopSound</code> ()
Stops the currently playing sound file.


### Method <code id="play-sound">playSound</code> (sound, startPoint)
Plays a custom sound file in-game

<b>Parameters:</b>

- <code><b>sound</b></code> string

  The sound file (without the file ending) you want to play
- <code><b>startPoint</b></code> float

  The start point in seconds at which the system should start playing

### Signal <code id="-speaker-sound">SpeakerSound</code> → type, sound
Triggers when the sound play state of the speaker pole changes.

<b>Parameters:</b>

- <code><b>type</b></code> integer

  The type of the speaker pole event.
- <code><b>sound</b></code> string

  The sound file including in the event.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>