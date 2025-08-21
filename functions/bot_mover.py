# functions.bot_mover.py

from models.mars_grid import MarsGrid
from models.bot import Bot
from models.directions import Direction
from models.moves import Move

def move_bot(mars_grid: MarsGrid, bot: Bot, moves: list[Move]):
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
                bot.is_lost = True
                break

def get_next_position(bot: Bot):
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
