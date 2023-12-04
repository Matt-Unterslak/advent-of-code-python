from typing import List

import numpy as np
from aocd.models import Puzzle

from tools.tools import pretty_print_nested_dict

YEAR: int = 2015
DAY: int = 20

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

BIG_NUM = 1000000


def get_first_house_to_receive_n_presents(
    number_of_presents: str, infinite_houses_enabled: bool = True
):
    number_of_presents = int(number_of_presents)
    houses = np.zeros(BIG_NUM)
    for elf in range(1, BIG_NUM):
        if infinite_houses_enabled:
            houses[elf::elf] += 10 * elf
        else:
            houses[elf : (elf + 1) * 50 : elf] += 11 * elf
    first_house = int(np.nonzero(houses >= number_of_presents)[0][0])
    return first_house


test_number_of_presents = "150"
print(
    f"{test_number_of_presents=}",
    get_first_house_to_receive_n_presents(test_number_of_presents),
)

print(puzzle.input_data)
part_a = get_first_house_to_receive_n_presents(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = get_first_house_to_receive_n_presents(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
