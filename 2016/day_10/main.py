import re
from collections import defaultdict
from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 10

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def add_value(name, value, bots, stack):
    bots[name].append(value)
    if len(bots[name]) == 2:
        stack.append(name)


def send_value(connection, value, bots, stack, outputs):
    out_type, out_name = connection
    if out_type == "bot":
        add_value(out_name, value, bots, stack)
    else:
        outputs[out_name].append(value)


def solve_bot_outputs(input_str: str, low_chip: int, high_chip: int):
    instructions: list[str] = input_str.split("\n")
    initial = [line.split() for line in instructions if line.startswith("value")]
    commands = [line.split() for line in instructions if not line.startswith("value")]

    connections = {}
    for line in commands:
        name, lower, higher = line[1], line[5:7], line[-2:]
        connections[name] = (lower, higher)

    bots = defaultdict(list)
    outputs = defaultdict(list)
    stack = []

    for line in initial:
        value, name = int(line[1]), line[-1]
        add_value(name, value, bots, stack)

    while stack:
        name = stack.pop()
        low_value, high_value = sorted(bots[name])
        if low_value == low_chip and high_value == high_chip:
            wanted_bot = name
        lower_connection, higher_connection = connections[name]
        send_value(lower_connection, low_value, bots, stack, outputs)
        send_value(higher_connection, high_value, bots, stack, outputs)
    a, b, c = (outputs[i][0] for i in "012")
    return wanted_bot, a * b * c


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, solve_bot_outputs(example.input_data, 2, 5))
    print(example.answer_b)
    print()

"""
    Submission A
"""
part_a = solve_bot_outputs(puzzle.input_data, 17, 61)[0]
print(part_a)
puzzle.answer_a = part_a


"""
    Submission B
"""
part_b = solve_bot_outputs(puzzle.input_data, 17, 61)[1]
print(part_b)
puzzle.answer_b = part_b
