"""
This module contains the logic for moving bots around the MarsGrid.
It updates the bot's position based on move instructions and tracks
lost positions to prevent repeated losses.
"""

from models.mars_grid import MarsGrid
from models.bot import Bot
from models.directions import Direction
from models.moves import Move
from models.position_move import PositionMove


def move_bot(mars_grid: MarsGrid, bot: Bot, moves: list[Move]):
    """
    Moves a bot according to a sequence of moves (L, R, F) on the MarsGrid.

    - Updates the bot’s position if within bounds.
    - Marks the bot as lost if it moves out of bounds and this position/direction
      hasn't previously caused a loss.
    - Skips move if the position/direction is known to result in a loss.

    Args:
        mars_grid (MarsGrid): The grid representing the Mars surface.
        bot (Bot): The bot to be moved.
        moves (list[Move]): A list of movement commands (Move Enum).
    """
    for move in moves:
        if move == Move.R:
            bot.direction = bot.direction.turn_right()
        elif move == Move.L:
            bot.direction = bot.direction.turn_left()
        elif move == Move.F:
            new_x, new_y = get_next_position(bot)

            if 0 <= new_x <= mars_grid.x_max and 0 <= new_y <= mars_grid.y_max:
                bot.x_position = new_x
                bot.y_position = new_y
            else:
                position_move = PositionMove(bot.x_position, bot.y_position, bot.direction)

                if mars_grid.is_position_move_lost(position_move):
                    continue  # Ignore the move — it's already known to be fatal

                bot.is_lost = True
                mars_grid.add_lost_position(position_move)
                break


def get_next_position(bot: Bot) -> tuple[int, int]:
    """
    Calculates the next (x, y) position for a bot based on its current direction.

    Args:
        bot (Bot): The bot whose next position is being determined.

    Returns:
        tuple[int, int]: The new x and y coordinates.
    """
    dx, dy = 0, 0

    if bot.direction == Direction.N:
        dy = 1
    elif bot.direction == Direction.E:
        dx = 1
    elif bot.direction == Direction.S:
        dy = -1
    elif bot.direction == Direction.W:
        dx = -1

    return bot.x_position + dx, bot.y_position + dy
