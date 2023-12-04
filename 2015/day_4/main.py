import hashlib
import re
from typing import List, Optional
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 4

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def create_md5_hash(input_str: str, regex_str: str) -> Optional[str]:
    m = hashlib.md5(input_str.encode("UTF-8"))
    hash_str = m.hexdigest()
    if re.search(regex_str, hash_str):
        return hash_str
    else:
        return None


def get_hashes(input_str: str, regex_str: str) -> int:
    hashes = [
        [create_md5_hash(input_str + str(i), regex_str), i]
        for i in range(0, 10000000)
        if create_md5_hash(input_str + str(i), regex_str) is not None
    ]
    if len(hashes) != 0:
        return hashes[0][1]
    else:
        return -1


for example in examples:
    print(example.input_data)
    print(example.answer_a, get_hashes(example.input_data, "^00000[0-9]"))
    print(example.answer_b)
    print()


part_a = get_hashes(puzzle.input_data, "^00000[0-9]")
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = get_hashes(puzzle.input_data, "^000000[0-9]")
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
