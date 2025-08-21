import pytest
from models.bot import Bot
from models.directions import Direction

def test_create_bot_valid():
    bot = Bot.create(1, 2, Direction.N)
    assert bot.x_position == 1
    assert bot.y_position == 2
    assert bot.direction == Direction.N
    assert bot.is_lost is False

def test_create_bot_invalid_x():
    with pytest.raises(ValueError, match="x_position must be an integer"):
        Bot.create("not-an-int", 2, Direction.N)

def test_create_bot_invalid_y():
    with pytest.raises(ValueError, match="y_position must be an integer"):
        Bot.create(1, "not-an-int", Direction.N)

def test_create_bot_invalid_direction():
    with pytest.raises(ValueError, match="direction must be an instance of Direction enum"):
        Bot.create(1, 2, "N")  # passing string instead of Direction enum

def test_get_position_not_lost():
    bot = Bot(3, 4, Direction.E, False)
    assert bot.get_position() == "3 4 E"

def test_get_position_lost():
    bot = Bot(3, 4, Direction.W, True)
    assert bot.get_position() == "3 4 W LOST"
