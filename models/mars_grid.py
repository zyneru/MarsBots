"""
Defines the MarsGrid class used to represent the surface area on which bots operate.

The grid has configurable maximum x and y boundaries, and it tracks coordinates where bots
have previously fallen off (gotten lost) to prevent future bots from making the same move.

A maximum grid size is enforced to comply with problem constraints.
"""

from dataclasses import dataclass, field
from models.position_move import PositionMove

MAX_GRID_SIZE = 50

@dataclass
class MarsGrid:
    """
    Represents the rectangular surface of Mars for the bot simulation.

    Attributes:
        x_max (int): The maximum x-coordinate of the grid.
        y_max (int): The maximum y-coordinate of the grid.
        lost_position_moves (set[PositionMove]): A set of PositionMove instances representing
                                                 moves that caused bots to be lost.

    Raises:
        ValueError: If x_max or y_max are out of allowed bounds (0 to MAX_GRID_SIZE).
    """
    x_max: int
    y_max: int
    lost_position_moves: set[PositionMove] = field(default_factory=set)

    def __post_init__(self):
        """
        Validates the x_max and y_max values after initialization.

        Raises:
            ValueError: If x_max or y_max are not integers or fall outside the allowed range [0, MAX_GRID_SIZE].
        """
        if not isinstance(self.x_max, int) or self.x_max < 0 or self.x_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's x_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.x_max}")
    
        if not isinstance(self.y_max, int) or self.y_max < 0 or self.y_max > MAX_GRID_SIZE:
            raise ValueError(f"Grid's y_max must be an integer between 0 and {MAX_GRID_SIZE}, got {self.y_max}")
        
    def add_lost_position(self, position_move: PositionMove):
        """
        Records a move that caused a bot to be lost, preventing future bots from making the same move.

        Args:
            position_move (PositionMove): The move that resulted in a bot being lost.

        Raises:
            ValueError: If position_move is not an instance of PositionMove.
        """
        if not isinstance(position_move, PositionMove):
            raise ValueError("position_move must be an instance of PositionMove")
        self.lost_position_moves.add(position_move)

    def is_position_move_lost(self, position_move: PositionMove) -> bool:
        """
        Checks if a move has previously caused a bot to be lost.

        Args:
            position_move (PositionMove): The move to check.

        Returns:
            bool: True if the move is known to result in a lost bot, False otherwise.

        Raises:
            ValueError: If position_move is not an instance of PositionMove.
        """
        if not isinstance(position_move, PositionMove):
            raise ValueError("position_move must be an instance of PositionMove")
        return position_move in self.lost_position_moves
