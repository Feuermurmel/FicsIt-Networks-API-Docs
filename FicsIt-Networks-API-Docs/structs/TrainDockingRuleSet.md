# Struct <code>TrainDockingRuleSet</code>

Contains information about the rules that describe when a train should depart from a station
## Instance Members
### Fields
- <code><b>definition</b></code> integer

  0 = Load/Unload Once, 1 = Fully Load/Unload
- <code><b>duration</b></code> float

  The amount of time the train will dock at least.
- <code><b>isDurationAndRule</b></code> boolean

  True if the duration of the train stop and the other rules have to be applied.
- <code><b>loadFilters</b></code> list of <a href="../classes/ItemType.md">ItemType</a>

  The types of items that will be loaded.
- <code><b>unloadFilters</b></code> list of <a href="../classes/ItemType.md">ItemType</a>

  The types of items that will be unloaded.