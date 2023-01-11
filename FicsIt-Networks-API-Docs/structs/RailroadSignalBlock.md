# Struct <code>RailroadSignalBlock</code>

A track section that combines the area between multiple signals.
## Instance Members
### Fields
- <code id="is-valid">isValid</code> boolean

  Is true if this signal block reference is valid.
- <code id="is-block-occupied">isBlockOccupied</code> boolean

  True if the block this signal is observing is currently occupied by a vehicle.
- <code id="has-block-reservation">hasBlockReservation</code> boolean

  True if the block this signal is observing has a reservation of a train e.g. will be passed by a train soon.
- <code id="is-path-block">isPathBlock</code> boolean

  True if the block this signal is observing is a path-block.
- <code id="block-validation">blockValidation</code> integer

  Returns the blocks validation status.
### Method <code id="is-occupied-by">isOccupiedBy</code> (train) → isOccupied
Allows you to check if this block is occupied by a given train.

<b>Parameters:</b>

- <code><b>train</b></code> <a href="../classes/Train.md">Train</a>

  The train you want to check if it occupies this block

<b>Return Values:</b>

- <code><b>isOccupied</b></code> boolean

  True if the given train occupies this block.