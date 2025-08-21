# MarsBots

MarsBots simulates the movement of robots on a rectangular Mars grid, following commands and reporting their final positions.

## Project Structure

- `marsbots.py`: Main entry point for running the simulation.
- `models/`: Contains core models:
  - [`models/bot.py`](models/bot.py): Bot representation.
  - [`models/directions.py`](models/directions.py): Direction enum and turning logic.
  - [`models/mars_grid.py`](models/mars_grid.py): Mars grid definition.
  - [`models/moves.py`](models/moves.py): Move enum and validation.
- `functions/`: Contains bot movement logic:
  - [`functions/bot_mover.py`](functions/bot_mover.py): Bot movement and position calculation.
- `sample_data.txt`: Example input and output.
- `tests/`: (Add your unit tests here.)

## How to Run

1. Ensure you have Python 3.11+ installed.
2. Set up your environment:
   ```
   export PYTHONPATH=.
   ```
   Or use the provided `.env` file.
3. Run the simulation:
   ```
   python marsbots.py
   ```
   Follow the prompts to enter grid size, bot positions, directions, and movement commands.

## Sample Input/Output

See [`sample_data.txt`](sample_data.txt) for example scenarios.