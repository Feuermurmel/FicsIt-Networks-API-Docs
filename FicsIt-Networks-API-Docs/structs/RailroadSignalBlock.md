# Struct <code>RailroadSignalBlock</code>

A track section that combines the area between multiple signals.
## Instance Members
### Fields
- <code><b>isValid</b></code> boolean

  Is true if this signal block reference is valid.
- <code><b>isBlockOccupied</b></code> boolean

  True if the block this signal is observing is currently occupied by a vehicle.
- <code><b>hasBlockReservation</b></code> boolean

  True if the block this signal is observing has a reservation of a train e.g. will be passed by a train soon.
- <code><b>isPathBlock</b></code> boolean

  True if the block this signal is observing is a path-block.
- <code><b>blockValidation</b></code> integer

  Returns the blocks validation status.
### Method <code>isOccupiedBy</code> (train) → isOccupied
Allows you to check if this block is occupied by a given train.

<b>Parameters:</b>

- <code><b>train</b></code> <a href="../classes/Train.md">Train</a>

  The train you want to check if it occupies this block

<b>Return Values:</b>

- <code><b>isOccupied</b></code> boolean

  True if the given train occupies this block.