import pytest
from models.bot import Bot
from models.directions import Direction
from models.mars_grid import MarsGrid
from models.moves import Move
from functions.bot_mover import move_bot


def test_move_bot_within_bounds():
    grid = MarsGrid(5, 5)
    bot = Bot.create(1, 1, Direction.N)
    moves = [Move.F, Move.R, Move.F, Move.L, Move.F]

    move_bot(grid, bot, moves)

    assert bot.x_position == 2
    assert bot.y_position == 3
    assert bot.direction == Direction.N
    assert not bot.is_lost


def test_move_bot_turns_only():
    grid = MarsGrid(3, 3)
    bot = Bot.create(1, 1, Direction.N)
    moves = [Move.R, Move.R, Move.L, Move.L]

    move_bot(grid, bot, moves)

    assert bot.x_position == 1
    assert bot.y_position == 1
    assert bot.direction == Direction.N
    assert not bot.is_lost


def test_move_bot_lost_off_grid():
    grid = MarsGrid(2, 2)
    bot = Bot.create(0, 0, Direction.S)
    moves = [Move.F]

    move_bot(grid, bot, moves)

    assert bot.is_lost
    assert bot.x_position == 0
    assert bot.y_position == 0


def test_move_bot_ignores_lost_move():
    grid = MarsGrid(2, 2)

    # First bot gets lost going South from (0,0)
    lost_bot = Bot.create(0, 0, Direction.S)
    move_bot(grid, lost_bot, [Move.F])
    assert lost_bot.is_lost

    # Second bot tries same move — should not get lost
    safe_bot = Bot.create(0, 0, Direction.S)
    move_bot(grid, safe_bot, [Move.F])
    assert not safe_bot.is_lost
    assert safe_bot.x_position == 0
    assert safe_bot.y_position == 0  # didn't move


def test_move_bot_multiple_directions_and_lost():
    grid = MarsGrid(3, 3)
    bot = Bot.create(3, 3, Direction.N)
    moves = [Move.F]

    move_bot(grid, bot, moves)

    assert bot.is_lost
    assert bot.x_position == 3
    assert bot.y_position == 3
