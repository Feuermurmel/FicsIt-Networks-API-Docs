# Class <code>SpeakerPole</code>

Superclasses: <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

This speaker pole allows to play custom sound files, In-Game
## Instance Members
<b>Inherited Members:</b>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>stopSound</code> () → 
Stops the currently playing sound file.


### Method <code>playSound</code> (sound, startPoint) → 
Plays a custom sound file in-game

<b>Parameters:</b>

- <code><b>sound</b></code> string

  The sound file (without the file ending) you want to play
- <code><b>startPoint</b></code> float

  The start point in seconds at which the system should start playing

### Signal <code>SpeakerSound</code> → type, sound
Triggers when the sound play state of the speaker pole changes.

<b>Parameters:</b>

- <code><b>type</b></code> integer

  The type of the speaker pole event.
- <code><b>sound</b></code> string

  The sound file including in the event.
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>