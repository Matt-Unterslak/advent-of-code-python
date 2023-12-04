from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 2

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

KEYPAD_3_BY_3 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

KEYPAD_5_BY_5 = [
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "],
]

"""
    Ref: Solution goes here
"""


def move_up(start_x, start_y, max_grid: int, keypad: list[list[str]]):
    if 0 <= start_y - 1 <= max_grid and keypad[start_x][start_y - 1] != " ":
        return start_y - 1
    else:
        return start_y


def move_down(start_x, start_y, max_grid: int, keypad: list[list[str]]):
    if 0 <= start_y + 1 <= max_grid and keypad[start_x][start_y + 1] != " ":
        return start_y + 1
    else:
        return start_y


def move_right(start_x, start_y, max_grid: int, keypad: list[list[str]]):
    if 0 <= start_x + 1 <= max_grid and keypad[start_x + 1][start_y] != " ":
        return start_x + 1
    else:
        return start_x


def move_left(start_x, start_y, max_grid: int, keypad: list[list[str]]):
    if 0 <= start_x - 1 <= max_grid and keypad[start_x - 1][start_y] != " ":
        return start_x - 1
    else:
        return start_x


def solve_keypad_3_by_3(input_str: str):
    instructions: list[str] = input_str.split("\n")
    start_location = [1, 1]
    max_grid: int = 2
    result = []
    for instruction in instructions:
        for direction in instruction:
            match direction:
                case "U":
                    start_location[0] = move_up(
                        start_location[1], start_location[0], max_grid, KEYPAD_3_BY_3
                    )
                case "D":
                    start_location[0] = move_down(
                        start_location[1], start_location[0], max_grid, KEYPAD_3_BY_3
                    )
                case "R":
                    start_location[1] = move_right(
                        start_location[1], start_location[0], max_grid, KEYPAD_3_BY_3
                    )
                case "L":
                    start_location[1] = move_left(
                        start_location[1], start_location[0], max_grid, KEYPAD_3_BY_3
                    )
        key_number = KEYPAD_3_BY_3[start_location[0]][start_location[1]]
        result.append(key_number)
    return "".join(result)


def solve_keypad_5_by_5(input_str: str):
    instructions: list[str] = input_str.split("\n")
    start_location = [2, 0]
    max_grid: int = 4
    result = []
    for instruction in instructions:
        for direction in instruction:
            match direction:
                case "U":
                    start_location[0] = move_up(
                        start_location[1], start_location[0], max_grid, KEYPAD_5_BY_5
                    )
                case "D":
                    start_location[0] = move_down(
                        start_location[1], start_location[0], max_grid, KEYPAD_5_BY_5
                    )
                case "R":
                    start_location[1] = move_right(
                        start_location[1], start_location[0], max_grid, KEYPAD_5_BY_5
                    )
                case "L":
                    start_location[1] = move_left(
                        start_location[1], start_location[0], max_grid, KEYPAD_5_BY_5
                    )

        key_number = KEYPAD_5_BY_5[start_location[0]][start_location[1]]
        result.append(key_number)
    return "".join([str(x) for x in result])


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, solve_keypad_3_by_3(example.input_data))
    print("5DB3", solve_keypad_5_by_5(example.input_data))
    print()

"""
    Submission A
"""
part_a = solve_keypad_3_by_3(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = solve_keypad_5_by_5(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
