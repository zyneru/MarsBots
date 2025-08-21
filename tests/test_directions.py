import pytest
from models.directions import Direction

def test_turn_right():
    assert Direction.N.turn_right() == Direction.E
    assert Direction.E.turn_right() == Direction.S
    assert Direction.S.turn_right() == Direction.W
    assert Direction.W.turn_right() == Direction.N

def test_turn_left():
    assert Direction.N.turn_left() == Direction.W
    assert Direction.W.turn_left() == Direction.S
    assert Direction.S.turn_left() == Direction.E
    assert Direction.E.turn_left() == Direction.N

def test_str_representation():
    assert str(Direction.N) == "N"
    assert str(Direction.E) == "E"
    assert str(Direction.S) == "S"
    assert str(Direction.W) == "W"
