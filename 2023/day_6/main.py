from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 6

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

"""
    Ref: Solution goes here
"""


def compute_number_of_winning_distances(time: int, distance_to_beat: int):
    ans = 0
    for x in range(time + 1):
        dx = x * (time - x)
        if dx >= distance_to_beat:
            ans += 1
    return ans


def binary_search_compute_number_of_winning_distances(time: int, distance_to_beat: int):
    # runs in O(log(t))
    # let g(x) = x*(t-x) is maximized at t//2
    # we want to know: what is the lowest value s.t. g(x) >= d
    # we want to know: what is the highest value s.t. g(x) >= d
    def g(x):
        return x * (time - x)

    lo = 0
    hi = time // 2
    if hi * (time - hi) < distance_to_beat:
        return 0
    assert g(lo) < distance_to_beat <= g(hi)
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if g(m) >= distance_to_beat:
            hi = m
        else:
            lo = m
    assert lo + 1 == hi
    assert g(lo) < distance_to_beat <= g(hi)
    first = hi
    assert g(first) >= distance_to_beat > g(first - 1)

    # g(x) == g(t-x), so there's symmetry about the midpoint t/2
    last = int((time / 2) + (time / 2 - first))
    assert (
        g(last) >= distance_to_beat > g(last + 1)
    ), f"last={last} g(last)={g(last)} {g(last + 1)} d={distance_to_beat}"
    return last - first + 1


def boat_race(input_str: str):
    times, distances = input_str.split("\n")
    times = [int(x) for x in times.strip("Time:").split()]
    distances = [int(x) for x in distances.strip("Distance:").split()]

    all_times = ""
    for t in times:
        all_times += str(t)
    all_times = int(all_times)
    all_distances = ""
    for d in distances:
        all_distances += str(d)
    all_distances = int(all_distances)

    product_of_winning_distances = 1
    for i in range(len(times)):
        product_of_winning_distances *= (
            binary_search_compute_number_of_winning_distances(times[i], distances[i])
        )

    total_winning_distances = binary_search_compute_number_of_winning_distances(
        all_times, all_distances
    )
    return product_of_winning_distances, total_winning_distances


"""
    Examples
"""
for example in examples:
    example_solutions = boat_race(example.input_data)
    print(example.input_data)
    print(352, example_solutions[0])
    print(example.answer_b, example_solutions[1])
    print()

solutions = boat_race(puzzle.input_data)
"""
    Submission A
"""
part_a = solutions[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = solutions[1]
print(part_b)
puzzle.answer_b = part_b
