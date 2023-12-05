from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 5

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


class FarmingMap:
    name: str
    map: dict[int, int]
    raw_map: list[list[int]]

    def __init__(self, map_str):
        name = map_str.split("\n")[0].strip(":")
        self.name = name
        lines = map_str.split("\n")[1:]
        # dst src size
        self.raw_map: list[list[int]] = [
            [int(x) for x in line.split()] for line in lines
        ]

    def print_map(self):
        print(f"{self.name=}")
        print(f"{self.raw_map=}")

    # deprecated: too slow with massive seed numbers
    def construct_map(self, max_seed: int):
        mapping: dict[int, int] = {i: i for i in range(1, max_seed + 1)}
        for dst, src, size in self.raw_map:
            for i in range(size):
                mapping[src + i] = dst + i
        self.map = mapping

    def lookup_destination(self, source):
        for dst, src, size in self.raw_map:
            if src <= source < src + size:
                return source + dst - src
        return source

    def lookup_destination_using_range(self, source_range: list[tuple[int, int]]):
        destinations = []
        for dest, src, sz in self.raw_map:
            src_end = src + sz
            new_range = []
            while source_range:
                (st, ed) = source_range.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    new_range.append(before)
                if inter[1] > inter[0]:
                    destinations.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    new_range.append(after)
            source_range = new_range
        return destinations + source_range


def process_almanac(input_str: str):
    sections: list[str] = input_str.split("\n\n")
    seeds = [int(x) for x in sections[0].split(":")[1].split()]
    maps: list[FarmingMap] = [FarmingMap(s) for s in sections[1:]]
    return seeds, maps


def find_min_location_part_1(input_str: str):
    seeds, maps = process_almanac(input_str)
    locations: list[int] = []
    for dest in seeds:
        for farm_map in maps:
            dest = farm_map.lookup_destination(dest)
        locations.append(dest)
    return min(locations)


def find_min_location_part_2(input_str: str):
    seeds, maps = process_almanac(input_str)
    locations: list[int] = []
    seed_pairs: list[tuple[int, int]] = list(zip(seeds[::2], seeds[1::2]))
    for start, size in seed_pairs:
        seed_range: list[tuple[int, int]] = [(start, start + size)]
        for farm_map in maps:
            seed_range = farm_map.lookup_destination_using_range(seed_range)

        locations.append(min(seed_range)[0])
    return min(locations)


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, find_min_location_part_1(example.input_data))
    print(46, find_min_location_part_2(example.input_data))
    print()

"""
    Submission A
# """
part_a = find_min_location_part_1(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = find_min_location_part_2(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
