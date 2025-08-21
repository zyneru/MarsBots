import builtins
import pytest
from io import StringIO
from contextlib import redirect_stdout
from marsbots import main

@pytest.mark.parametrize("inputs, expected_outputs", [
    (
        [
            "5 3",          # Mars grid max coordinates
            "1 1 E",        # Bot 1 start
            "RFRFRFRF",     # Bot 1 moves
            "Y",            # Add another bot
            "3 2 N",        # Bot 2 start
            "FRRFLLFFRRFLL",# Bot 2 moves
            "Y",            # Add another bot
            "0 3 W",        # Bot 3 start
            "LLFFFLFLFL",   # Bot 3 moves
            "N"             # Do not add more bots
        ],
        [
            "1 1 E",
            "3 3 N LOST",
            "2 3 S"
        ]
    )
])
def test_integration_main(monkeypatch, inputs, expected_outputs):
    input_iter = iter(inputs)
    outputs = []

    def fake_input(prompt=""):
        return next(input_iter)

    def fake_print(*args, **kwargs):
        outputs.append(" ".join(str(a) for a in args))

    monkeypatch.setattr(builtins, "input", fake_input)
    monkeypatch.setattr(builtins, "print", fake_print)

    main()

    # The prints include prompts and other messages, filter only the bot position lines
    # We expect only the lines printed by `print(bot.get_position())` in main
    position_lines = [line for line in outputs if any(ch.isdigit() for ch in line) and ("LOST" in line or len(line.split()) == 3)]

    assert position_lines == expected_outputs
