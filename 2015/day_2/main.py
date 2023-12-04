from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 2

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def calculate_wrapping_area(input_data: str) -> int:
    l, b, h = [int(x) for x in input_data.split("x")]
    surface_area: int = (l * b * 2) + (b * h * 2) + (l * h * 2)
    slack: int = min(l * b, b * h, l * h)
    return surface_area + slack


def calculate_total_wrapping_area(input_data: str) -> int:
    packages = input_data.split("\n")
    total = sum([calculate_wrapping_area(package) for package in packages])
    return total


for example in examples:
    print(example.input_data, calculate_wrapping_area(example.input_data))
    print(example.answer_a)
    print(example.answer_b)
    print()

# print(puzzle.input_data)

part_a = calculate_total_wrapping_area(puzzle.input_data)
print(part_a)
print("---------------------")
print()
puzzle.answer_a = part_a

samples = [
    ["2x3x4", 34],
    ["1x1x10", 14],
]


def calculate_ribbon(input_data: str) -> int:
    l, b, h = sorted([int(x) for x in input_data.split("x")])
    wrapping_ribbon = 2 * l + 2 * b
    bow_ribbon = l * b * h
    return wrapping_ribbon + bow_ribbon


def calculate_total_ribbon(input_data: str) -> int:
    packages = input_data.split("\n")
    total = sum([calculate_ribbon(package) for package in packages])
    return total


for sample in samples:
    print(sample[0])
    print(sample[1], calculate_ribbon(sample[0]))
    print()

part_b = calculate_total_ribbon(puzzle.input_data)
print(part_b)
print("---------------------")
print()
puzzle.answer_b = part_b
