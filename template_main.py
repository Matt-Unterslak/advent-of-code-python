from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 6

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


for example in examples:
    print(example.input_data)
    print(example.answer_a)
    print(example.answer_b)
    print()


# part_a = number_of_nice_strings(puzzle.input_data, True)
# print(part_a)
# puzzle.answer_a = part_a
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

# part_b = number_of_nice_strings(puzzle.input_data, False)
# print(part_b)
# puzzle.answer_b = part_b
print("---------------------")
print()
