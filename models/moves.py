"""
Module defining the Move enumeration and validation utility for move commands.
"""

# models/moves.py

from enum import Enum

MAX_MOVES = 100

class Move(Enum):
    """
    Enumeration representing possible move commands for a bot.

    Members:
        R (int): Turn right.
        L (int): Turn left.
        F (int): Move forward.
    """
    R = 1
    L = 2
    F = 3


def validate_moves(moves_input: str):
    """
    Validate and convert a string of move commands into a list of Move enums.

    Args:
        moves_input (str): A string representing a sequence of move commands,
                        e.g. "RFLF".

    Returns:
        list[Move]: List of Move enum members corresponding to the input commands.

    Raises:
        KeyError: If any character in moves_input does not correspond to a Move enum member.
        ValueError: If the move command string exceeds 100 moves.
    """

    if len(moves_input) > MAX_MOVES:
        raise ValueError("Move command string cannot exceed 100 moves")

    moves = []
    for move_input in moves_input:
        moves.append(Move[move_input])
    return moves
