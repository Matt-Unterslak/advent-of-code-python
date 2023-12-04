from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 1

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def blocks(input_str: str) -> tuple[int, int]:
    instructions = [(x[:1], int(x[1:])) for x in input_str.split(", ")]

    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    facing = 0
    pos = (0, 0)
    visited = []
    visited_twice = []
    found_twice_visited = False
    for turn, step in instructions:
        facing += 1 if turn == "R" else -1
        facing %= 4
        while step > 0:
            pos = pos[0] + steps[facing][0], pos[1] + steps[facing][1]
            if pos in visited:
                visited_twice.append(pos)
                found_twice_visited = True
            if not found_twice_visited:
                visited.append(pos)
            step -= 1

    if len(visited_twice) > 0:
        return abs(pos[0]) + abs(pos[1]), (
            abs(visited_twice[0][0]) + abs(visited_twice[0][1])
        )
    else:
        return abs(pos[0]) + abs(pos[1]), 0


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, blocks(example.input_data)[0])
    print(example.answer_b)
    print()

"""
    Submission A
"""
part_a = blocks(puzzle.input_data)[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = blocks(puzzle.input_data)[1]
print(part_b)
puzzle.answer_b = part_b
