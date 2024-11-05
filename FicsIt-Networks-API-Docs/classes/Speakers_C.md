# Class <code>Speakers_C</code>

Superclasses: <a href="SpeakerPole.md">SpeakerPole</a> < <a href="FGBuildable.md">FGBuildable</a> < <a href="Actor.md">Actor</a> < <a href="Object.md">Object</a>

The FicsIt-Networks speaker pole is a network component which allows you to use one more sense of the pioneers to give commands to them or to just make ambient better.

The speaker pole can play sound files located in the Computer Folder "/Sounds" in your Satisfactory Save-Games-Folder. The FicsIt-Networks speaker pole is only able to play .ogg files cause FicsIt Inc. has the opinion other file formates are useless.
## Instance Members
<b>Inherited Members:</b>
- SpeakerPole: <a href="SpeakerPole.md#user-content--speaker-sound">SpeakerSound</a>, <a href="SpeakerPole.md#user-content-play-sound">playSound()</a>, <a href="SpeakerPole.md#user-content-stop-sound">stopSound()</a>
- Actor: <a href="Actor.md#user-content-get-factory-connectors">getFactoryConnectors()</a>, <a href="Actor.md#user-content-get-inventories">getInventories()</a>, <a href="Actor.md#user-content-get-network-connectors">getNetworkConnectors()</a>, <a href="Actor.md#user-content-get-pipe-connectors">getPipeConnectors()</a>, <a href="Actor.md#user-content-get-power-connectors">getPowerConnectors()</a>, <a href="Actor.md#user-content-location">location</a>, <a href="Actor.md#user-content-rotation">rotation</a>, <a href="Actor.md#user-content-scale">scale</a>
- Object: <a href="Object.md#user-content-get-hash">getHash()</a>, <a href="Object.md#user-content-get-type">getType()</a>, <a href="Object.md#user-content-hash">hash</a>, <a href="Object.md#user-content-internal-name">internalName</a>, <a href="Object.md#user-content-internal-path">internalPath</a>
### Method <code id="set-volume">setVolume</code> (Volume)


<b>Parameters:</b>

- <code><b>Volume</b></code> float

  

### Method <code id="set-range">setRange</code> (Range)


<b>Parameters:</b>

- <code><b>Range</b></code> float

  

### Method <code id="get-volume">getVolume</code> () → Volume



<b>Return Values:</b>

- <code><b>Volume</b></code> float

  
### Method <code id="get-range">getRange</code> () → Range



<b>Return Values:</b>

- <code><b>Range</b></code> float

  
### Signal <code id="-speaker-setting">SpeakerSetting</code> → setting, New, OLD


<b>Parameters:</b>

- <code><b>setting</b></code> integer

  
- <code><b>New</b></code> float

  
- <code><b>OLD</b></code> float

  
## Static Members
<b>Inherited Members:</b>
- Object: <a href="Object.md#user-content-s-get-hash">getHash()</a>, <a href="Object.md#user-content-s-get-type">getType()</a>, <a href="Object.md#user-content-s-hash">hash</a>, <a href="Object.md#user-content-s-internal-name">internalName</a>, <a href="Object.md#user-content-s-internal-path">internalPath</a>