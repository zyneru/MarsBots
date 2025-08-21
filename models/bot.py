"""
models/bot.py

Defines the Bot class used to represent a robot on a Mars exploration grid.
Each bot maintains its current position, direction, and lost status.
Includes validation logic during creation and a method to report position.
"""

from dataclasses import dataclass
from models.directions import Direction

@dataclass
class Bot:
    """
    Represents a bot operating on the Mars grid.

    Attributes:
        x_position (int): The bot's current X coordinate.
        y_position (int): The bot's current Y coordinate.
        direction (Direction): The direction the bot is facing (N, E, S, W).
        is_lost (bool): Whether the bot is lost after falling off the grid.
    """

    x_position: int
    y_position: int
    direction: Direction
    is_lost: bool

    @classmethod
    def create(cls, x: int, y: int, direction: Direction):
        """
        Creates a new bot with the given position and direction.

        Args:
            x (int): The starting X coordinate.
            y (int): The starting Y coordinate.
            direction (Direction): The starting direction.

        Returns:
            Bot: A new instance of Bot with is_lost set to False.

        Raises:
            ValueError: If x or y is not an integer, or if direction is not a valid Direction.
        """
        if not isinstance(x, int):
            raise ValueError(f"x_position must be an integer, got {x}")
        if not isinstance(y, int):
            raise ValueError(f"y_position must be an integer, got {y}")
        if not isinstance(direction, Direction):
            raise ValueError("direction must be an instance of Direction enum")
        return cls(x, y, direction, False)
    
    def get_position(self):
        """
        Returns a formatted string representing the bot's current position and status.

        Returns:
            str: The bot's position in the format "x y direction [LOST]".
        """
        position = f"{self.x_position} {self.y_position} {self.direction}"
        if self.is_lost:
            position += " LOST"
        return position
