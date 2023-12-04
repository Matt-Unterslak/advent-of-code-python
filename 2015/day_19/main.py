import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 19

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def process_input(input_str: str) -> tuple[list[str], str]:
    processed_input = [x for x in input_str.split("\n") if x != ""]
    replacements = processed_input[0:-1]
    input_molecule = processed_input[-1]
    return replacements, input_molecule


def calculate_number_of_distinct_molecules(input_str: str):
    replacements, input_molecule = process_input(input_str)
    final_combinations = set()
    for replacement in replacements:
        match, _, replace = replacement.split(" ")
        indices = [m.start() for m in re.finditer(match, input_molecule)]
        lm = len(match)
        final_combinations.update(
            [input_molecule[:i] + replace + input_molecule[i + lm :] for i in indices]
        )
    return len(final_combinations)


def calculate_minimum_fabrication_steps(input_str: str):
    replacements, medicine = process_input(input_str)

    # LHS, RHS sorted with largest LHS first
    replacements = [(l.split()[-1], l.split()[0]) for l in replacements if "=>" in l]
    replacements.sort(key=lambda x: len(x[0]))  # sort by string length
    replacements = replacements[::-1]  # reverse

    total = 0
    while medicine != "e":
        for lhs, rhs in replacements:
            if lhs in medicine:
                medicine = medicine.replace(lhs, rhs, 1)
                total += 1
                break

    return total


answers = [3, 6]
part_b_inputs = [
    "e => H\ne => O\nH => HO\nH => OH\nO => HH\n\nHOH",
    "e => H\ne => O\nH => HO\nH => OH\nO => HH\n\nHOHOHO",
]
for ind, example in enumerate(examples):
    print(example.input_data)
    print(example.answer_a, calculate_number_of_distinct_molecules(example.input_data))
    print(
        answers[ind],
        calculate_minimum_fabrication_steps(part_b_inputs[ind]),
    )
    print()


part_a = calculate_number_of_distinct_molecules(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()


part_b = calculate_minimum_fabrication_steps(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
