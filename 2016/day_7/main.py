import re
from typing import List
from aocd.models import Puzzle

from tools.input_processor import process_input_multiline

YEAR: int = 2016
DAY: int = 7

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def find_abba(word: str) -> bool:
    for i in range(0, len(word) - 3):
        tmp = word[i : i + 4]
        if tmp == tmp[::-1] and len(set(tmp)) == 2:
            return True
    return False


def process_input(input_str: str) -> tuple[int, list[str], list[str]]:
    ips: list[str] = process_input_multiline(input_str)
    ips: list[list[str]] = [re.split(r"\[|\]", d) for d in ips]
    supernet: list[str] = [" ".join(d[::2]) for d in ips]
    hypernet: list[str] = [" ".join(d[1::2]) for d in ips]
    return len(ips), supernet, hypernet


def count_valid_tls_ips(input_str: str) -> int:
    total_ips, supernet, hypernet = process_input(input_str)
    tls_ips: int = 0
    for j in range(total_ips):
        abba_in_hypernet: bool = find_abba(hypernet[j])
        abba_in_supernet: bool = find_abba(supernet[j])
        if abba_in_supernet and not abba_in_hypernet:
            tls_ips += 1

    return tls_ips


def find_aba_bab(supernet: str, hypernet: str):
    for i in range(0, len(supernet) - 2):
        tmp = supernet[i : i + 3]
        if tmp == tmp[::-1] and len(set(tmp)) == 2:
            aba = tmp[1] + tmp[0] + tmp[1]
            if len(re.findall(aba, hypernet)) > 0:
                return True
    return False


def count_valid_ssl_ips(input_str: str) -> int:
    total_ips, supernet, hypernet = process_input(input_str)
    ssl_ips: int = 0
    for j in range(total_ips):
        if find_aba_bab(supernet[j], hypernet[j]):
            ssl_ips += 1

    return ssl_ips


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, count_valid_tls_ips(example.input_data))
    print(example.answer_b)
    print()


"""
    Submission A
"""
part_a = count_valid_tls_ips(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a


"""
    Samples for Part B
"""

inputs = [
    "aba[bab]xyz",
    "xyx[xyx]xyx",
    "aaa[kek]eke",
    "zazbz[bzb]cdb",
]
results = [
    1,
    0,
    1,
    1,
]
for sample in inputs:
    print(sample)
    print(count_valid_ssl_ips(sample))
    print()

"""
    Submission B
"""
part_b = count_valid_ssl_ips(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
