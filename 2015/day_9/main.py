import itertools
import json
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 9

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def extract_paths(input_str: str):
    paths = [
        [
            x.split(" to ")[0],
            x.split(" to ")[1].split(" = ")[0],
            int(x.split(" to ")[1].split(" = ")[1]),
        ]
        for x in input_str.split("\n")
    ]
    paths += [[city_2, city_1, distance] for city_1, city_2, distance in paths]
    return paths


def get_location_permutations(paths: list[list[str, str, int]]):
    locations = [city_1 for city_1, city_2, distance in paths]
    locations += [city_2 for city_1, city_2, distance in paths]
    locations = list(set(locations))
    list(itertools.permutations(locations))
    return list(itertools.permutations(locations))


def construct_routes(paths: list[list[str, str, int]]) -> dict[str, dict[str, int]]:
    routes: dict[str, dict[str, int]] = {}
    for city_1, city_2, distance in paths:
        if city_1 not in routes:
            routes[city_1] = {city_2: distance}
        else:
            existing_routes = routes[city_1]
            if city_2 not in existing_routes:
                existing_routes[city_2] = distance
            routes[city_1] = existing_routes
    return routes


def get_permutation_distance(
    permutation: tuple, all_routes: dict[str, dict[str, int]]
) -> int:
    total_distance: int = 0
    for i in range(len(permutation) - 1):
        city_1 = permutation[i]
        city_2 = permutation[i + 1]
        distance = all_routes.get(city_1).get(city_2)
        total_distance += distance
    return total_distance


def get_all_permutation_distances(
    permutations: list[tuple], all_routes: dict[str, dict[str, int]]
) -> tuple[dict[tuple, int], list[tuple, int], list[tuple, int]]:
    shortest_distance = 99999999999999
    shortest_route: list[tuple, int] = []

    longest_distance = 0
    longest_route: list[tuple, int] = []

    all_distances: dict[tuple, int] = {}
    for permutation in permutations:
        distance = get_permutation_distance(permutation, all_routes)
        all_distances[permutation] = distance
        if distance < shortest_distance:
            shortest_route: list[tuple, int] = [permutation, distance]
            shortest_distance = distance
        if distance > longest_distance:
            longest_route: list[tuple, int] = [permutation, distance]
            longest_distance = distance
    return all_distances, shortest_route, longest_route


def get_all_possible_route_distances(input_str: str):
    paths: list[list[str, str, int]] = extract_paths(input_str)
    routes: dict[str, dict[str, int]] = construct_routes(paths)

    permutations = get_location_permutations(paths)
    all_route_distances, shortest_route, longest_route = get_all_permutation_distances(
        permutations, routes
    )

    result = {
        "all_routes": all_route_distances,
        "shortest_route": shortest_route,
        "longest_route": longest_route,
    }
    return result


for example in examples:
    print(example.input_data)
    print(
        example.answer_a,
        get_all_possible_route_distances(example.input_data).get("shortest_route")[1],
    )
    print(
        982,
        get_all_possible_route_distances(example.input_data).get("longest_route")[1],
    )
    print()


part_a = get_all_possible_route_distances(puzzle.input_data).get("shortest_route")[1]
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()


part_b = get_all_possible_route_distances(puzzle.input_data).get("longest_route")[1]
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
