import re
from typing import List

import numpy as np
from aocd.models import Puzzle

from tools.tools import create_grid_as_numpy_array, print_numpy_array

YEAR: int = 2016
DAY: int = 8

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def convert_grid_to_screen(grid: np.ndarray):
    aa = []
    for i in range(0, len(grid.T)):
        aa.append("".join([str(x) for x in grid.T[i]]))
        # print(aa[i])
    for a in aa:
        a = a.replace("1", "█")
        a = a.replace("0", "░")
        print(a)


def get_screen_result(input_str: str, grid_rows: int, grid_columns: int):
    screen: np.ndarray = create_grid_as_numpy_array(
        rows=grid_rows, columns=grid_columns
    )
    instructions: list[str] = input_str.split("\n")
    # print_numpy_array(screen, "screen")
    for instruction in instructions:
        # print(f"{instruction=}")
        if instruction.startswith("rect"):
            a, b = [int(x) for x in instruction.strip("rect ").split("x")]
            screen[:b, :a] = 1
        elif instruction.startswith("rotate"):
            row_or_column, row_or_column_index_and_step = instruction.split("=")
            if "row" in row_or_column:
                row_index, step = [
                    int(x) for x in row_or_column_index_and_step.split(" by ")
                ]
                screen[row_index, :] = np.roll(screen[row_index, :], step)
            else:
                column_index, step = [
                    int(x) for x in row_or_column_index_and_step.split(" by ")
                ]
                screen[:, column_index] = np.roll(screen[:, column_index], step)

    # print_numpy_array(screen, "screen")
    # convert_grid_to_screen(screen)
    return int(np.sum(screen))


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, get_screen_result(example.input_data, 3, 7))
    print(example.answer_b)
    print()

"""
    Submission A
"""
part_a = get_screen_result(puzzle.input_data, 6, 50)
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""

data = puzzle.input_data.split("\n")
grid = np.zeros((6, 50), dtype="int16")
for d in data:
    nums = [int(num) for num in re.findall(r"\d+", d)]
    if "rect" in d:
        x = nums[0]
        y = nums[1]
        grid[:y, :x] = 1
    elif "row" in d:
        y = nums[0]
        val = nums[1]
        # grid[y,:] = np.roll(grid[y,:], val)
        grid[y] = np.roll(grid[y], val)
    elif "col" in d:
        x = nums[0]
        val = nums[1]
        grid[:, x] = np.roll(grid[:, x], val)
# print(grid.sum())

aa = []
for i in range(0, len(grid.T)):
    aa.append("".join([str(x) for x in grid.T[i]]))
    # print(aa[i])
for a in aa:
    a = a.replace("1", "█")
    a = a.replace("0", "░")
    print(a)

# EOARGPHYAO
