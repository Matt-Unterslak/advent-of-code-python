from collections import defaultdict
from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 3

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def engine_schematic(input_str: str):
    lines: list[str] = input_str.split("\n")
    grid: list[list[str]] = [[c for c in line] for line in lines]
    rows: int = len(grid)
    columns: int = len(grid[0])

    total_engine_parts = 0
    part_numbers: defaultdict = defaultdict(list)

    for row in range(rows):
        gears = set()  # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for col in range(len(grid[row]) + 1):
            if col < columns and grid[row][col].isdigit():
                # this quick hack allows me not to have to chain numbers together.
                # Each time I encounter a number in the same row, the previous number shifts
                # one decimal place over
                n = n * 10 + int(grid[row][col])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= row + rr < rows and 0 <= col + cc < columns:
                            char = grid[row + rr][col + cc]
                            if not char.isdigit() and char != ".":
                                has_part = True
                            if char == "*":
                                gears.add((row + rr, col + cc))
            elif n > 0:
                for gear in gears:
                    part_numbers[gear].append(n)
                if has_part:
                    total_engine_parts += n
                n = 0
                has_part = False
                gears = set()

    total_gear_ratios = 0
    for k, v in part_numbers.items():
        if len(v) == 2:
            total_gear_ratios += v[0] * v[1]
    return total_engine_parts, total_gear_ratios


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, engine_schematic(example.input_data)[0])
    print(example.answer_b, engine_schematic(example.input_data)[1])
    print()
#
solutions = engine_schematic(puzzle.input_data)
"""
    Submission A
"""
part_a = solutions[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = solutions[1]
print(part_b)
puzzle.answer_b = part_b
