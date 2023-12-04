import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 5

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

VOWELS = ["a", "e", "i", "o", "u"]
NAUGHT_STRINGS = ["ab", "cd", "pq", "xy"]


def naughty_or_nice_part_1(input_str: str) -> int:
    if (
        len([x for x in input_str if x in VOWELS]) > 2
        and not any(x in input_str for x in NAUGHT_STRINGS)
        and re.search(r"([a-z])\1", input_str)
    ):
        return 1
    return 0


def check_two_letters_appear_more_than_once(
    input_str: str, double_letter: str
) -> tuple[bool, str]:
    times_appear = input_str.count(double_letter)
    if times_appear > 1:
        return True, double_letter
    else:
        return False, double_letter


def naughty_or_nice_part_2(input_str: str) -> int:
    if len(re.findall(r"([a-z]{2}).*\1", input_str)) and re.findall(
        r"([a-z]).\1", input_str
    ):
        return 1
    return 0


def number_of_nice_strings(input_str: str, is_part_1: bool) -> int:
    inputs = input_str.split("\n")
    if is_part_1:
        naughty_or_nice_inputs = [naughty_or_nice_part_1(x) for x in inputs]
    else:
        naughty_or_nice_inputs = [naughty_or_nice_part_2(x) for x in inputs]
    nice_words = [x for x in naughty_or_nice_inputs if x == 1]
    return len(nice_words)


for example in examples:
    print(example.input_data)
    print(example.answer_a, naughty_or_nice_part_1(example.input_data))
    print(example.answer_b)
    print()


part_a = number_of_nice_strings(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

samples = [
    ["qjhvhtzxzqqjkmpb", 1],
    ["xxyxx", 1],
    ["uurcxstgmygtbstg", 0],
    ["ieodomkazucvgmuy", 0],
]
for sample in samples:
    print(sample[0])
    print(sample[1], number_of_nice_strings(sample[0], False))
    print()

part_b = number_of_nice_strings(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
