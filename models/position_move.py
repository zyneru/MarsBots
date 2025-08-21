"""
models/position_move.py

Defines the PositionMove dataclass which represents a position and direction
on the Mars grid. This class is immutable (frozen) and used to track positions
where a bot has been lost.
"""

from dataclasses import dataclass
from models.directions import Direction

@dataclass(frozen=True)
class PositionMove:
    """
    Represents a position and facing direction on the Mars grid.

    Attributes:
        x (int): The X coordinate on the grid.
        y (int): The Y coordinate on the grid.
        direction (Direction): The facing direction at the position.
    """

    x: int
    y: int
    direction: Direction

    def __post_init__(self):
        """
        Validates that x and y are integers and direction is a Direction instance.

        Raises:
            ValueError: If x or y is not an integer or if direction is not a Direction.
        """
        if not isinstance(self.x, int):
            raise ValueError(f"x must be an integer, got {self.x}")
        if not isinstance(self.y, int):
            raise ValueError(f"y must be an integer, got {self.y}")
        if not isinstance(self.direction, Direction):
            raise ValueError(f"direction must be a direction, got {self.direction}")
