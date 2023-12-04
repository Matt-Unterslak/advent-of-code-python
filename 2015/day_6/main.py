import numpy as np
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 6

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def update_lights_based_on_instruction_part_1(input_str: str, grid):
    input_str = input_str.split()
    # Turn on/off
    if input_str[0] == "turn":
        x1, y1 = input_str[2].split(",")
        x2, y2 = input_str[4].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if input_str[1] == "on":
            grid[x1 : x2 + 1, y1 : y2 + 1] = 1
        else:
            assert input_str[1] == "off"
            grid[x1 : x2 + 1, y1 : y2 + 1] = 0
    # Toggle
    else:
        assert input_str[0] == "toggle"
        x1, y1 = input_str[1].split(",")
        x2, y2 = input_str[3].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1 : x2 + 1, y1 : y2 + 1] = np.logical_not(grid[x1 : x2 + 1, y1 : y2 + 1])
    return grid


def update_lights_based_on_instruction_part_2(input_str: str, grid):
    input_str = input_str.split()
    # Turn on/off
    if input_str[0] == "turn":
        x1, y1 = input_str[2].split(",")
        x2, y2 = input_str[4].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if input_str[1] == "on":
            grid[x1 : x2 + 1, y1 : y2 + 1] += 1
        else:
            assert input_str[1] == "off"
            grid[x1 : x2 + 1, y1 : y2 + 1] -= 1
            grid[grid < 0] = 0
    # Toggle
    else:
        assert input_str[0] == "toggle"
        x1, y1 = input_str[1].split(",")
        x2, y2 = input_str[3].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1 : x2 + 1, y1 : y2 + 1] += 2
    return grid


def update_lights(input_str: str, is_part_1: bool):
    grid = np.zeros((1000, 1000), "int32")
    inputs = input_str.split("\n")
    for x in inputs:
        if is_part_1:
            grid = update_lights_based_on_instruction_part_1(x, grid)
        else:
            grid = update_lights_based_on_instruction_part_2(x, grid)
    return int(np.sum(grid))


for example in examples:
    print(example.input_data)
    print(example.answer_a, update_lights(example.input_data, True))
    print(example.answer_b, update_lights(example.input_data, False))
    print()


part_a = update_lights(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = update_lights(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
