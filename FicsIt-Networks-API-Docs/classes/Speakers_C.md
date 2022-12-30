# Class <code>Speakers_C</code>

Superclasses: <a href="SpeakerPole.md">SpeakerPole</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The FICSIT-Networks speaker pole is a network component which allows you to use one more sense of the pioneers to give commands to them or to just make ambient better.

The speaker pole can play sound files located in the Computer Folder "/Sounds" in your Satisfactory Save-Games-Folder. The FICSIT-Networks speaker pole is only able to play .ogg files cause FICSIT Inc. has the opinion other file formates are useless.
## Instance Members
<b>Inherited Members:</b>
- SpeakerPole: <a href="SpeakerPole.md#SpeakerSound">SpeakerSound</a>, <a href="SpeakerPole.md#playSound">playSound()</a>, <a href="SpeakerPole.md#stopSound">stopSound()</a>
- Actor: <a href="Actor.md#getFactoryConnectors">getFactoryConnectors()</a>, <a href="Actor.md#getInventories">getInventories()</a>, <a href="Actor.md#getNetworkConnectors">getNetworkConnectors()</a>, <a href="Actor.md#getPipeConnectors">getPipeConnectors()</a>, <a href="Actor.md#getPowerConnectors">getPowerConnectors()</a>, <a href="Actor.md#location">location</a>, <a href="Actor.md#rotation">rotation</a>, <a href="Actor.md#scale">scale</a>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>
### Method <code>setVolume(Volume) -> </code>


<b>Parameters:</b>

- <code><b>Volume</b></code> float

  
### Method <code>setRange(Range) -> </code>


<b>Parameters:</b>

- <code><b>Range</b></code> float

  
### Method <code>getVolume() -> Volume</code>


<b>Return Values:</b>

- <code><b>Volume</b></code> float

  
### Method <code>getRange() -> Range</code>


<b>Return Values:</b>

- <code><b>Range</b></code> float

  
### Signal <code>SpeakerSetting -> setting, New, OLD</code>


<b>Parameters:</b>

- <code><b>setting</b></code> integer

  
- <code><b>New</b></code> float

  
- <code><b>OLD</b></code> float

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#getHash">getHash()</a>, <a href="Object.md#getType">getType()</a>, <a href="Object.md#hash">hash</a>, <a href="Object.md#internalName">internalName</a>, <a href="Object.md#internalPath">internalPath</a>