import json
from typing import List, Optional
from aocd.models import Puzzle

from tools.input_processor import process_input_multiline

YEAR: int = 2015
DAY: int = 16

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

keys = [
    "number",
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes",
]
ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def setup_sues() -> dict[str, dict[str, Optional[int]]]:
    sues = {}
    for i in range(1, 501):
        sue = {}
        for key in keys:
            if key == "number":
                sue[key] = str(i)
            else:
                sue[key] = None
        sues[str(i)] = sue
    return sues


def process_input(input_str: str):
    sues: dict[str, dict[str, Optional[int]]] = setup_sues()
    for item in process_input_multiline(input_str):
        sue_data = [x.split(":") for x in item.strip("Sue ").split(",")]
        sue_number = sue_data[0][0]
        sue_data = [sue_data[0][1:]] + sue_data[1:]
        sue = sues[sue_number]

        for key, val in sue_data:
            sue[key.strip()] = int(val.strip())
    return sues


def detective_function_1(sues: dict[str, dict[str, Optional[int]]]):
    for _, sue in sues.items():
        matched = True
        checker = list(sue.keys())
        checker = [x for x in checker if x != "number"]
        for i in checker:
            if sue[i] is not None and sue[i] != ticker_tape[i]:
                matched = False
                break
        if matched is True:
            return sue


def detective_function_2(sues: dict[str, dict[str, Optional[int]]]):
    for _, sue in sues.items():
        matched = True
        checker = list(sue.keys())
        checker = [x for x in checker if x != "number"]
        for i in checker:
            if i in ["cats", "trees"]:
                if sue[i] is not None and sue[i] <= ticker_tape[i]:
                    matched = False
                    break
            elif i in ["pomeranians", "goldfish"]:
                if sue[i] is not None and sue[i] >= ticker_tape[i]:
                    matched = False
                    break
            elif sue[i] is not None and sue[i] != ticker_tape[i]:
                matched = False
                break
        if matched is True:
            return sue


def find_the_aunt_who_sent_the_gift(input_str: str, is_part_1: bool):
    sues: dict[str, dict[str, Optional[int]]] = process_input(input_str)
    if is_part_1:
        sue = detective_function_1(sues)
        return sue["number"]
    else:
        sue = detective_function_2(sues)
        return sue["number"]


for example in examples:
    print(example.input_data)
    print(example.answer_a)
    print(example.answer_b)
    print()

print(puzzle.input_data)
part_a = find_the_aunt_who_sent_the_gift(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = find_the_aunt_who_sent_the_gift(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
