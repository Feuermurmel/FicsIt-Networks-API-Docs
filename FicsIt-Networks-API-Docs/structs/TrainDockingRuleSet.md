# Struct <code>TrainDockingRuleSet</code>

Contains infromation about the rules that descibe when a trian should depart from a station
## Instance Members
### Fields
- <code id="definition">definition</code> integer

  0 = Load/Unload Once, 1 = Fully Load/Unload
- <code id="duration">duration</code> float

  The amount of time the train will dock at least.
- <code id="is-duration-and-rule">isDurationAndRule</code> boolean

  True if the duration of the train stop and the other rules have to be applied.
- <code id="load-filters">loadFilters</code> list of <a href="../classes/ItemType.md">ItemType</a>

  The types of items that will be loaded.
- <code id="unload-filters">unloadFilters</code> list of <a href="../classes/ItemType.md">ItemType</a>

  The types of items that will be unloaded.