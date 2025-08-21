# models/bot.py

from dataclasses import dataclass
from models.directions import Direction

@dataclass
class Bot:
    x_position: int
    y_position: int
    direction: Direction
    is_lost: bool

    @classmethod
    def create(cls, x: int, y: int, direction: Direction):
        if not isinstance(x, int):
            raise ValueError(f"x_position must be an integer, got {x}")
        if not isinstance(y, int):
            raise ValueError(f"y_position must be an integer, got {y}")
        if not isinstance(direction, Direction):
            raise ValueError("direction must be an instance of Direction enum")
        return cls(x, y, direction, False)
    
    def get_position(self):
        position = f"{self.x_position} {self.y_position} {self.direction}"
        if (self.is_lost):
            position += " LOST"
        return position
        