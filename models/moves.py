# models/moves.py

from enum import Enum

class Move(Enum):
    R = 1
    L = 2
    F = 3


def validate_moves(moves_input: str):
    moves = []
    for move_input in moves_input:
        moves.append(Move[move_input])
    return moves