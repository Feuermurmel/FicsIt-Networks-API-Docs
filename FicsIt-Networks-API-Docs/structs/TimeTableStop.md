# Struct <code>TimeTableStop</code>

Information about a train stop in a time table.
## Instance Members
### Fields
- <code><b>station</b></code> <a href="../classes/RailroadStation.md">RailroadStation</a>

  The station at which the train should stop
### Method <code>getRuleSet</code> () → ruleset
Returns The rule set wich describe when the train will depart from the train station.

<b>Return Values:</b>

- <code><b>ruleset</b></code> <a href="TrainDockingRuleSet.md">TrainDockingRuleSet</a>

  The rule set of this time table stop.
### Method <code>setRuleSet</code> (ruleset) → 
Allows you to change the Rule Set of this time table stop.

<b>Parameters:</b>

- <code><b>ruleset</b></code> <a href="TrainDockingRuleSet.md">TrainDockingRuleSet</a>

  The rule set you want to use instead.