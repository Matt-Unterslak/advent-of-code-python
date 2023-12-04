from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 3

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def get_final_direction(
    current_location: tuple[int, int], direction: str
) -> tuple[int, int]:
    match direction:
        case "^":
            return current_location[0], current_location[1] + 1
        case "v":
            return current_location[0], current_location[1] - 1
        case ">":
            return current_location[0] + 1, current_location[1]
        case "<":
            return current_location[0] - 1, current_location[1]


def get_total_houses(input_data: str) -> list[tuple[int, int]]:
    grid_locations = [(0, 0)]
    current_grid = (0, 0)
    for x in input_data:
        current_grid = get_final_direction(current_grid, x)
        if current_grid not in grid_locations:
            grid_locations.append(current_grid)
    return grid_locations


def get_total_houses_part_1(input_data: str) -> int:
    return len(get_total_houses(input_data))


def get_total_houses_part_2(input_data: str) -> int:
    santa_input = "".join([x for i, x in enumerate(input_data) if i % 2 == 0])
    robot_input = "".join([x for i, x in enumerate(input_data) if i % 2 != 0])
    santa_houses = get_total_houses(santa_input)
    robot_houses = get_total_houses(robot_input)

    missing_houses = [x for x in robot_houses if x not in santa_houses]
    total_houses = santa_houses + missing_houses
    return len(total_houses)


for example in examples:
    print(example.input_data)
    print(example.answer_a, get_total_houses_part_1(example.input_data))
    print(example.answer_b)
    print()


part_a = get_total_houses_part_1(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

samples = [
    ["^v", 3],
    ["^>v<", 3],
    ["^v^v^v^v^v", 11],
]
for sample in samples:
    print(sample[0])
    print(sample[1], get_total_houses_part_2(sample[0]))
    print()

part_b = get_total_houses_part_2(puzzle.input_data)
print(part_b)
print("---------------------")
print()
puzzle.answer_b = part_b
