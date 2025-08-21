# models/marsgrid.py

from dataclasses import dataclass, field
from models.position_move import PositionMove

MAX_GRID_SIZE = 50

@dataclass
class MarsGrid:
    x_max: int
    y_max: int
    lost_position_moves: set[PositionMove] = field(default_factory=set)

    def __post_init__(self):
        if not isinstance(self.x_max, int) or self.x_max < 0 or self.x_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's x_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.x_max}")
    
        if not isinstance(self.y_max, int) or self.y_max < 0 or self.y_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's y_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.y_max}")
        
    def add_lost_position(self, position_move: PositionMove):
        if not isinstance(position_move, PositionMove):
            raise ValueError("position_move must be an instance of PositionMove")
        self.lost_position_moves.add(position_move)

    def is_position_move_lost(self, position_move: PositionMove) -> bool:
        if not isinstance(position_move, PositionMove):
            raise ValueError("position_move must be an instance of PositionMove")
        return position_move in self.lost_position_moves
