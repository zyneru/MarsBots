"""
models/directions.py

Defines the Direction enumeration representing the four cardinal compass points.
Includes methods to turn left or right relative to the current direction.
"""

from enum import Enum

class Direction(Enum):
    """
    Enumeration for the four cardinal directions: North, East, South, and West.

    Provides methods to turn left or right, cycling through the directions.

    Members:
        N (Direction): North.
        E (Direction): East.
        S (Direction): South.
        W (Direction): West.
    """

    N = 1
    E = 2
    S = 3
    W = 4

    def turn_right(self):
        """
        Returns the direction obtained by turning 90 degrees to the right (clockwise).

        Returns:
            Direction: The new direction after turning right.
        """
        members = list(Direction)
        index = (members.index(self) + 1) % len(members)
        return members[index]

    def turn_left(self):
        """
        Returns the direction obtained by turning 90 degrees to the left (counter-clockwise).

        Returns:
            Direction: The new direction after turning left.
        """
        members = list(Direction)
        index = (members.index(self) - 1) % len(members)
        return members[index]

    def __str__(self):
        """
        Returns:
            str: The name of the direction (e.g., 'N', 'E', 'S', 'W').
        """
        return self.name
