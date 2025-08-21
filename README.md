# MarsBots

MarsBots simulates the movement of robots on a rectangular Mars grid, following commands and reporting their final positions.

## Project Structure

- `marsbots.py`: Main entry point for running the simulation.
- `models/`: Contains core models:
  - [`models/bot.py`](models/bot.py): Bot representation.
  - [`models/directions.py`](models/directions.py): Direction enum and turning logic.
  - [`models/mars_grid.py`](models/mars_grid.py): Mars grid definition and lost position tracking.
  - [`models/moves.py`](models/moves.py): Move enum and validation.
  - [`models/position_move.py`](models/position_move.py): Position and move tracking for lost bots.
- `functions/`: Contains bot movement logic:
  - [`functions/bot_mover.py`](functions/bot_mover.py): Bot movement and position calculation.
- `sample_data.txt`: Example input and output.
- `tests/`: Contains unit and integration tests.

## How to Run

1. Ensure you have Python 3.11+ installed.
2. Set up your environment:
   ```
   export PYTHONPATH=.
   ```
   (On Windows, use `set` instead of `export`.)
3. Run the simulation:
   ```
   py marsbots.py
   ```
   Follow the prompts to enter grid size, bot positions, directions, and movement commands.

## Sample Input/Output

### Sample Input
```
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```
- The first line defines the upper-right coordinates of the Mars grid.
- Each bot is defined by two lines:
  - Starting position and direction (`x y D`).
  - Movement commands as a string of letters (`R`, `L`, `F`) where:
    - `R` = turn right,
    - `L` = turn left,
    - `F` = move forward.

### Sample Output
```
1 1 E
3 3 N LOST
2 3 S
```

- The output shows the final position and direction of each bot.
- If a bot moves off the grid, it is marked as `LOST` at the last valid position.

## Notes

- The grid size is validated to be between 0 and 50.
- Bots that move off the grid are marked as "LOST" and their last position is tracked to prevent future bots from being lost at the same spot.
- Move commands are validated; invalid moves or directions will prompt for re-entry.
- The simulation supports multiple bots sequentially, allowing you to add bots until you choose to stop