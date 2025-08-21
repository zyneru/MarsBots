import builtins
import pytest
from models.directions import Direction
from models.moves import Move
from models.mars_grid import MarsGrid
from marsbots import capture_grid, capture_bot, capture_moves

def test_capture_grid_value_error(monkeypatch, capsys):
    # Simulate invalid input causing ValueError (e.g. non-integer input)
    inputs = iter(["a b"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = capture_grid()
    captured = capsys.readouterr()
    assert result is None
    assert "Invalid input for MarsGrid dimensions" in captured.out

def test_capture_bot_value_error(monkeypatch, capsys):
    grid = MarsGrid(5, 5)
    # Simulate invalid integer inputs for bot position (non-int)
    inputs = iter(["x y N"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = capture_bot(grid)
    captured = capsys.readouterr()
    assert result is None
    assert "Invalid bot values entered" in captured.out

def test_capture_bot_key_error(monkeypatch, capsys):
    grid = MarsGrid(5, 5)
    # Simulate invalid direction input that is not in Direction enum
    inputs = iter(["1 1 Z"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = capture_bot(grid)
    captured = capsys.readouterr()
    assert result is None
    assert "Invalid direction" in captured.out

def test_capture_moves_key_error(monkeypatch, capsys):
    # Simulate invalid move character that is not in Move enum
    inputs = iter(["XYZ"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    result = capture_moves()
    captured = capsys.readouterr()
    assert result is None
    assert "Invalid move input" in captured.out
