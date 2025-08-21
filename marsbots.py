from models.bot import Bot
from models.directions import Direction
from models.mars_grid import MarsGrid
from models.mars_grid import MAX_GRID_SIZE
from models.moves import Move
from models.moves import validate_moves
from functions.bot_mover import move_bot

def capture_grid() -> MarsGrid | None:
    try:
        print("Enter the upper-right coordinates of the rectangular world ")
        x_max_input, y_max_input = input(f"format x y (max {MAX_GRID_SIZE} {MAX_GRID_SIZE}): ").split()
        return MarsGrid(int(x_max_input), int(y_max_input))
    except ValueError as e:
        print(f"Invalid input for MarsGrid dimensions: {e}")
        return None

def create_bot_on_grid(x: int, y: int, direction: Direction, grid: MarsGrid) -> Bot | None:
    if not 0 <= x <= grid.x_max or not 0 <= y <= grid.y_max:
        raise ValueError(
            f"Starting position ({x}, {y}) out of grid bounds ({grid.x_max}, {grid.y_max})"
        )
    return Bot.create(x, y, direction)

def capture_bot(mars_grid: MarsGrid) -> Bot | None:
    try:
        print("Enter the starting coordinates and facing direction for the bot: ")

        bot_x_input, bot_y_input, bot_direction_input = input(
            f"format x y d (x max: {mars_grid.x_max} y max: {mars_grid.y_max}): "
        ).upper().split()

        return create_bot_on_grid(
            int(bot_x_input), int(bot_y_input), Direction[bot_direction_input], mars_grid
        )
    except ValueError as e:
        print(f"Invalid bot values entered: {e}")
    except KeyError:
        print(f"Invalid direction: '{bot_direction_input}'. Must be one of {[d.name for d in Direction]}")

    return None

def capture_moves() -> list[Move] | None:
    try:
        moves_input = input("Enter the bot's move command: ").upper()
        return validate_moves(moves_input)
    except KeyError:
        print(f"Invalid move input: '{moves_input}'. Each move must be one of {[m.name for m in Move]}")

    return None


def main():
    mars_grid = None
    while mars_grid is None:
        mars_grid = capture_grid()

    add_bot = "Y"
    while add_bot == "Y":
        bot = None
        while bot is None:
            bot = capture_bot(mars_grid)

        moves = None
        while moves is None:
            moves = capture_moves()

        move_bot(mars_grid, bot, moves)
        print(bot.get_position())
        add_bot = input("Add another bot Y/N?").upper()

if __name__ == "__main__":
    main()
