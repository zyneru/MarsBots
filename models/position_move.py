# models/position_move.py

from dataclasses import dataclass
from models.directions import Direction

@dataclass(frozen=True)
class PositionMove:
    x: int
    y: int
    direction: Direction

    def __post_init__(self):
        if not isinstance(self.x, int):
            raise ValueError(f"x must be an integer, got {self.x}")
        if not isinstance(self.y, int):
            raise ValueError(f"y must be an integer, got {self.y}")
        if not isinstance(self.direction, Direction):
            raise ValueError(f"direction must be a direction, got {self.direction}")
