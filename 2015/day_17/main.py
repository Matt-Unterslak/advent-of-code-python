import re
from itertools import combinations, permutations
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 17

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def calculate_permutations(input_str: str, total_liters: int):
    buckets = [int(x) for x in re.findall(r"-?\d+", input_str)]
    all_valid_combinations = []
    for i in range(len(buckets)):
        valid_combinations = [
            x for x in combinations(buckets, i) if sum(x) == total_liters
        ]
        all_valid_combinations += valid_combinations
    return len(all_valid_combinations)


def calculate_minimum_permutations(input_str: str, total_liters: int):
    buckets = [int(x) for x in re.findall(r"-?\d+", input_str)]
    all_valid_combinations = []
    for i in range(len(buckets)):
        valid_combinations = [
            x for x in combinations(buckets, i) if sum(x) == total_liters
        ]
        all_valid_combinations += valid_combinations

    minimum_buckets = min([len(x) for x in all_valid_combinations])
    minimum_combinations = [
        x for x in all_valid_combinations if len(x) == minimum_buckets
    ]
    return len(minimum_combinations)


for example in examples:
    print(example.input_data)
    print(example.answer_a, calculate_permutations(example.input_data, 25))
    print(example.answer_b, calculate_minimum_permutations(example.input_data, 25))
    print()


part_a = calculate_permutations(puzzle.input_data, 150)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

# samples = [
#     ["qjhvhtzxzqqjkmpb", 1],
#     ["xxyxx", 1],
#     ["uurcxstgmygtbstg", 0],
#     ["ieodomkazucvgmuy", 0],
# ]
# for sample in samples:
#     print(sample[0])
#     print(sample[1])
#     print()

part_b = calculate_minimum_permutations(puzzle.input_data, 150)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
