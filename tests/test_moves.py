import pytest
from models.moves import Move, validate_moves

def test_validate_moves_valid():
    moves_str = "RLF"
    moves = validate_moves(moves_str)
    assert moves == [Move.R, Move.L, Move.F]

def test_validate_moves_empty():
    moves = validate_moves("")
    assert moves == []

def test_validate_moves_invalid():
    with pytest.raises(KeyError):
        validate_moves("RX")  # 'X' is not a valid move

def test_validate_moves_max_length():
    valid_moves = "R" * 100  # exactly 100 moves, should pass
    moves = validate_moves(valid_moves)
    assert len(moves) == 100
    assert all(isinstance(m, Move) for m in moves)

    too_long_moves = "R" * 101  # 101 moves, should raise ValueError
    with pytest.raises(ValueError, match="cannot exceed 100 moves"):
        validate_moves(too_long_moves)