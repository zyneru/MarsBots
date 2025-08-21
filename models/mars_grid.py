# models/marsgrid.py

from dataclasses import dataclass

MAX_GRID_SIZE = 50

@dataclass
class MarsGrid:
    x_max: int
    y_max: int

    def __post_init__(self):
        if not isinstance(self.x_max, int) or self.x_max < 0 or self.x_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's x_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.x_max}")
    
        if not isinstance(self.y_max, int) or self.y_max < 0 or self.y_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's y_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.y_max}")