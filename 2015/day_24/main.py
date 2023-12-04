import itertools
from math import prod
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 24

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def get_package_groupings_to_balance_the_sleigh(input_str: str, number_of_groups: int):
    package_weights: list[int] = [int(x) for x in input_str.split("\n")]
    print(package_weights)
    total_weight: int = sum(package_weights)
    group_weight: int = int(total_weight / number_of_groups)
    print(total_weight, group_weight)

    quanta: list[list[int]] = []
    minimum_packages = 888
    for packages_per_group in range(1, 10):
        for group in itertools.combinations(package_weights, packages_per_group):
            if sum(group) == group_weight:
                if len(group) < minimum_packages:
                    minimum_packages = len(group)
                quanta.append([group, len(group), prod(group)])
                break
    quantum_entanglements: list[int] = [
        x[2] for x in quanta if x[1] == minimum_packages
    ]
    return min(quantum_entanglements)


answer_b = 44
for example in examples:
    print(example.input_data)
    print(
        example.answer_a,
        get_package_groupings_to_balance_the_sleigh(example.input_data, 3),
    )
    print(answer_b, get_package_groupings_to_balance_the_sleigh(example.input_data, 4))
    print()


part_a = get_package_groupings_to_balance_the_sleigh(puzzle.input_data, 3)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = get_package_groupings_to_balance_the_sleigh(puzzle.input_data, 4)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
