import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 8

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def process_str(string: str) -> str:
    string_contents = string.strip('"')
    string_contents = re.sub(r'\\"', '"', string_contents)
    string_contents = string_contents.replace("\\\\", "\\")
    string_contents = re.sub(r"\\x[a-zA-Z0-9][a-zA-Z0-9]", "1", string_contents)
    return string_contents


def get_difference_between_code_size_and_memory_size(input_str: str):
    total_size: int = 0
    memory_size: int = 0
    for x in input_str.split("\n"):
        total_size += len(x)
        memory_size += len(eval(x))

        # if len(eval(x)) != len(process_str(x)):
        #     print(x, eval(x), process_str(x))
    return total_size - memory_size


def encode_string(original_str: str):
    encoded_str = original_str.replace("\\", "\\\\")
    encoded_str = encoded_str.replace('"', '\\"')
    encoded_str = '"' + encoded_str + '"'
    return encoded_str


def encode_input_string(input_str: str):
    total_size: int = 0
    original_size: int = 0
    for x in input_str.split("\n"):
        original_size += len(x)
        total_size += len(encode_string(x))
    return total_size - original_size


for example in examples:
    print(example.input_data)
    print("_________________")
    print(
        example.answer_a,
        get_difference_between_code_size_and_memory_size(example.input_data),
    )
    print(19, encode_input_string(example.input_data))

    print("_________________")
    print()


part_a = get_difference_between_code_size_and_memory_size(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = encode_input_string(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
