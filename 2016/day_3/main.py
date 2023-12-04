import itertools
from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 3

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

"""
    Ref: Solution goes here
"""


def valid_triangle(side_1: int, side_2: int, side_3: int):
    if (
        side_1 + side_2 > side_3
        and side_1 + side_3 > side_2
        and side_2 + side_3 > side_1
    ):
        return True
    else:
        return False


def find_valid_triangles(input_str: str, is_part_1: bool) -> int:
    triangles: list[list[str]] = [x.split() for x in input_str.split("\n")]
    print(len(triangles))
    valid_triangles: list[list[int]] = []
    if is_part_1:
        for a, b, c in triangles:
            if valid_triangle(int(a), int(b), int(c)):
                valid_triangles.append([int(a), int(b), int(c)])

    else:
        for row in range(0, len(triangles), 3):
            for column in range(3):
                a: int = int(triangles[row][column])
                b: int = int(triangles[row + 1][column])
                c: int = int(triangles[row + 2][column])
                if valid_triangle(a, b, c):
                    valid_triangles.append([a, b, c])
    return len(valid_triangles)


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, find_valid_triangles(example.input_data, True))
    print(example.answer_b)
    print()

"""
    Submission A
"""
part_a = find_valid_triangles(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a


"""
    Submission B
"""
part_b = find_valid_triangles(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
