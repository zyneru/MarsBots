import pytest
from models.position_move import PositionMove
from models.directions import Direction

def test_position_move_valid():
    pm = PositionMove(5, 10, Direction.N)
    assert pm.x == 5
    assert pm.y == 10
    assert pm.direction == Direction.N

def test_position_move_invalid_x():
    with pytest.raises(ValueError, match="x must be an integer"):
        PositionMove("not-an-int", 10, Direction.N)

def test_position_move_invalid_y():
    with pytest.raises(ValueError, match="y must be an integer"):
        PositionMove(5, "not-an-int", Direction.N)

def test_position_move_invalid_direction():
    with pytest.raises(ValueError, match="direction must be a direction"):
        PositionMove(5, 10, "N")  # passing string instead of Direction enum
