import collections
import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 6

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def process_word_to_columns(
    input_str: str, start_pos: int, end_pos: int, columns: list[str]
) -> list[str]:
    column_index = 0
    for i in range(start_pos, end_pos):
        columns[column_index] += input_str[i]
        column_index += 1
    return columns


def decode_message(input_str: str):
    separated = re.finditer(r"\n", input_str)
    columns: list[str] = ["" for _ in range(1000)]
    start_index: int = 0
    for val in separated:
        break_index: int = val.start()
        columns = process_word_to_columns(input_str, start_index, break_index, columns)
        start_index = break_index + 1

    columns = process_word_to_columns(input_str, start_index, len(input_str), columns)
    columns_to_consider = [x for x in columns if x != ""]
    most_common_characters = [
        collections.Counter(x).most_common()[0][0] for x in columns_to_consider
    ]
    least_common_characters = [
        collections.Counter(x).most_common()[-1][0] for x in columns_to_consider
    ]

    return "".join(most_common_characters), "".join(least_common_characters)


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print()
    print(example.answer_a, decode_message(example.input_data)[0])
    print("advent", decode_message(example.input_data)[1])
    print()

"""
    Submission A
"""
part_a = decode_message(puzzle.input_data)[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = decode_message(puzzle.input_data)[1]
print(part_b)
puzzle.answer_b = part_b
