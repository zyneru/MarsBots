"""
Mars Bot Simulator

This module provides a command-line interface to simulate the movement of robots ("bots") on a
rectangular grid representing the surface of Mars.

Features:
- Captures grid dimensions for the rectangular Mars surface.
- Allows placing bots on the grid with an initial position and facing direction.
- Accepts movement commands for each bot to simulate navigation.
- Tracks bots that move off the grid (lost bots).
- Prints final positions of bots after executing all movement commands.
- Handles user input errors and validates inputs for grid size, bot positioning, directions, and moves.

Usage:
Run the module directly and follow prompts to:
    1. Set grid dimensions.
    2. Place one or more bots on the grid.
    3. Input movement commands for each bot.
    4. View final positions of bots, with indication if any are lost.

Dependencies:
- models.bot.Bot
- models.directions.Direction
- models.mars_grid.MarsGrid
- models.moves.Move, validate_moves
- functions.bot_mover.move_bot

"""

from models.bot import Bot
from models.directions import Direction
from models.mars_grid import MarsGrid
from models.mars_grid import MAX_GRID_SIZE
from models.moves import Move
from models.moves import validate_moves
from models.moves import MAX_MOVES
from functions.bot_mover import move_bot

def capture_grid() -> MarsGrid | None:
    """
    Prompt the user to input the upper-right coordinates of the Mars grid.

    Returns:
        MarsGrid: A MarsGrid object initialized with the provided coordinates.
        None: If the input is invalid or cannot be parsed.
    """
    try:
        print("Enter the upper-right coordinates of the rectangular world ")
        x_max_input, y_max_input = input(f"format x y (max {MAX_GRID_SIZE} {MAX_GRID_SIZE}): ").split()
        return MarsGrid(int(x_max_input), int(y_max_input))
    except ValueError as e:
        print(f"Invalid input for MarsGrid dimensions: {e}")
        return None

def create_bot_on_grid(x: int, y: int, direction: Direction, grid: MarsGrid) -> Bot | None:
    """
    Create a Bot instance on the specified grid at the given coordinates and direction.

    Args:
        x (int): The x-coordinate of the bot's starting position.
        y (int): The y-coordinate of the bot's starting position.
        direction (Direction): The initial facing direction of the bot.
        grid (MarsGrid): The MarsGrid instance representing the grid boundaries.

    Raises:
        ValueError: If the starting position is out of the grid bounds.

    Returns:
        Bot: A new Bot instance positioned on the grid.
    """
    if not 0 <= x <= grid.x_max or not 0 <= y <= grid.y_max:
        raise ValueError(
            f"Starting position ({x}, {y}) out of grid bounds ({grid.x_max}, {grid.y_max})"
        )
    return Bot.create(x, y, direction)

def capture_bot(mars_grid: MarsGrid) -> Bot | None:
    """
    Prompt the user to enter the starting coordinates and facing direction for a bot.

    Args:
        mars_grid (MarsGrid): The grid on which the bot will be placed.

    Returns:
        Bot: A Bot instance initialized with the user input.
        None: If input is invalid or out of bounds.
    """
    try:
        print("Enter the starting coordinates and facing direction for the bot: ")

        bot_x_input, bot_y_input, bot_direction_input = input(
            f"format x y d (x max: {mars_grid.x_max} y max: {mars_grid.y_max}): "
        ).upper().split()

        return create_bot_on_grid(
            int(bot_x_input), int(bot_y_input), Direction[bot_direction_input], mars_grid
        )
    except ValueError as e:
        print(f"Invalid bot values entered: {e}")
    except KeyError:
        print(f"Invalid direction: '{bot_direction_input}'. Must be one of {[d.name for d in Direction]}")

    return None

def capture_moves() -> list[Move] | None:
    """
    Prompt the user to enter the sequence of move commands for a bot.

    Returns:
        list[Move]: A list of Move enum members representing the moves.
        None: If the input contains invalid move commands.
    """
    try:
        moves_input = input(f"Enter the bot's move command (max: {MAX_MOVES}): ").upper()
        return validate_moves(moves_input)
    except KeyError:
        print(f"Invalid move input: '{moves_input}'. Each move must be one of {[m.name for m in Move]}")

    return None

def main():
    """
    Main application loop for running the Mars bot simulation.
    It prompts for grid size, then iteratively captures bots and their move commands,
    executes their moves, and prints the final positions.
    """
    mars_grid = None
    while mars_grid is None:
        mars_grid = capture_grid()

    add_bot = "Y"
    while add_bot == "Y":
        bot = None
        while bot is None:
            bot = capture_bot(mars_grid)

        moves = None
        while moves is None:
            moves = capture_moves()

        move_bot(mars_grid, bot, moves)
        print(bot.get_position())
        add_bot = input("Add another bot Y/N?").upper()

if __name__ == "__main__":
    main()
