import ast
import json
import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 12

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def sum_of_item(item, skip_red: bool = False):
    if isinstance(item, list):
        return sum([sum_of_item(i, skip_red) for i in item])

    if isinstance(item, dict):
        if skip_red and "red" in item.values():
            return 0
        return sum([sum_of_item(i, skip_red) for i in item.values()])

    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item


def find_sum_of_input(input_str: str, skip_red: bool = False):
    item = json.loads(input_str)
    return sum_of_item(item, skip_red)


for example in examples:
    print(example.input_data)
    print(example.answer_a, find_sum_of_input(example.input_data))
    print(example.answer_b)
    print()

part_a = find_sum_of_input(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

samples = [
    ["[1,2,3]", 6],
    ['[1,{"c":"red","b":2},3]', 4],
    ['{"d":"red","e":[1,2,3,4],"f":5}', 0],
    ['[1,"red",5]', 6],
]
for sample in samples:
    print(sample[0])
    print(sample[1], find_sum_of_input(sample[0], True))
    print()

part_b = find_sum_of_input(puzzle.input_data, True)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
