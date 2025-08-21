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
