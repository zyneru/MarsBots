import pytest
from models.mars_grid import MarsGrid, MAX_GRID_SIZE
from models.position_move import PositionMove
from models.directions import Direction

def test_marsgrid_valid_creation():
    grid = MarsGrid(10, 20)
    assert grid.x_max == 10
    assert grid.y_max == 20
    assert isinstance(grid.lost_position_moves, set)
    assert len(grid.lost_position_moves) == 0

@pytest.mark.parametrize("x_max", [-1, MAX_GRID_SIZE + 1, "not-int"])
def test_marsgrid_invalid_x_max(x_max):
    with pytest.raises(ValueError, match="Grid's x_max must be an integer"):
        MarsGrid(x_max, 10)

@pytest.mark.parametrize("y_max", [-1, MAX_GRID_SIZE + 1, "not-int"])
def test_marsgrid_invalid_y_max(y_max):
    with pytest.raises(ValueError, match="Grid's y_max must be an integer"):
        MarsGrid(10, y_max)

def test_add_lost_position_and_check():
    grid = MarsGrid(5, 5)
    pos_move = PositionMove(2, 2, Direction.N)
    grid.add_lost_position(pos_move)
    assert pos_move in grid.lost_position_moves
    assert grid.is_position_move_lost(pos_move) is True

def test_is_position_move_lost_not_present():
    grid = MarsGrid(5, 5)
    pos_move = PositionMove(1, 1, Direction.E)
    assert grid.is_position_move_lost(pos_move) is False

def test_add_lost_position_invalid_type():
    grid = MarsGrid(5, 5)
    with pytest.raises(ValueError, match="position_move must be an instance of PositionMove"):
        grid.add_lost_position("not-a-position-move")

def test_is_position_move_lost_invalid_type():
    grid = MarsGrid(5, 5)
    with pytest.raises(ValueError, match="position_move must be an instance of PositionMove"):
        grid.is_position_move_lost(123)
