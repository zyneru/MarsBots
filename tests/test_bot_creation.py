import pytest
from models.directions import Direction
from models.mars_grid import MarsGrid
from marsbots import create_bot_on_grid

def test_create_bot_on_grid_position_out_of_bounds():
    grid = MarsGrid(5, 5)

    # x less than 0
    with pytest.raises(ValueError, match="Starting position \\(-1, 0\\) out of grid bounds"):
        create_bot_on_grid(-1, 0, Direction.N, grid)

    # y less than 0
    with pytest.raises(ValueError, match="Starting position \\(0, -1\\) out of grid bounds"):
        create_bot_on_grid(0, -1, Direction.N, grid)

    # x greater than grid max
    with pytest.raises(ValueError, match="Starting position \\(6, 0\\) out of grid bounds"):
        create_bot_on_grid(6, 0, Direction.N, grid)

    # y greater than grid max
    with pytest.raises(ValueError, match="Starting position \\(0, 6\\) out of grid bounds"):
        create_bot_on_grid(0, 6, Direction.N, grid)
