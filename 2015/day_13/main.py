import itertools
import json
import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 13

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def extract_seating_happiness(input_str: str):
    seating_happiness: list[list[str, str, int]] = []
    for item in input_str.split("\n"):
        value = int(re.findall(r"-?\d+", item)[0])
        if "lose" in item:
            value *= -1

        person_1 = item.split()[0]
        person_2 = item.split()[-1].strip(".")
        seating_happiness.append([person_1, person_2, value])
    return seating_happiness


def add_myself_to_plans(
    seating_happiness: list[list[str, str, int]], people: list[str]
) -> list[list[str, str, int]]:
    me = "me"
    my_happiness = 0
    for person in people:
        seating_happiness.append([me, person, my_happiness])
        seating_happiness.append([person, me, my_happiness])
    people.append(me)
    return seating_happiness


def get_set_of_people(seating_happiness: list[list[str, str, int]]):
    people = [person_1 for person_1, person_2, happiness_value in seating_happiness]
    people += [person_2 for person_1, person_2, happiness_value in seating_happiness]
    return list(set(people))


def get_people_permutations(
    seating_happiness: list[list[str, str, int]], people: list[str]
):
    return list(itertools.permutations(people))


def construct_seating_options(
    seating_happiness: list[list[str, str, int]]
) -> dict[str, dict[str, int]]:
    seating_options: dict[str, dict[str, int]] = {}
    for person_1, person_2, distance in seating_happiness:
        if person_1 not in seating_options:
            seating_options[person_1] = {person_2: distance}
        else:
            existing_options = seating_options[person_1]
            if person_2 not in existing_options:
                existing_options[person_2] = distance
            seating_options[person_1] = existing_options
    return seating_options


def get_permutation_happiness(
    permutation: tuple, seating_options: dict[str, dict[str, int]]
) -> int:
    total_happiness: int = 0
    for i in range(len(permutation) - 1):
        person_1 = permutation[i]
        person_2 = permutation[i + 1]
        happiness_value_1 = seating_options.get(person_1).get(person_2)
        happiness_value_2 = seating_options.get(person_2).get(person_1)
        total_happiness += happiness_value_1 + happiness_value_2

    # last person seated compared with first person seated as this is a round table
    person_1 = permutation[0]
    person_2 = permutation[-1]
    happiness_value_1 = seating_options.get(person_1).get(person_2)
    happiness_value_2 = seating_options.get(person_2).get(person_1)
    total_happiness += happiness_value_1 + happiness_value_2
    return total_happiness


def get_all_seating_plans(
    permutations: list[tuple], seating_options: dict[str, dict[str, int]]
) -> tuple[dict[tuple, int], list[tuple, int], list[tuple, int]]:
    least_happiness = 99999999999999
    least_happy_seating_plan: list[tuple, int] = []

    happiest_seating = 0
    happiest_seating_plan: list[tuple, int] = []

    all_seating_happiness: dict[tuple, int] = {}
    for permutation in permutations:
        # print(permutation)
        happiness_value = get_permutation_happiness(permutation, seating_options)
        all_seating_happiness[permutation] = happiness_value
        if happiness_value < least_happiness:
            least_happy_seating_plan: list[tuple, int] = [permutation, happiness_value]
            least_happiness = happiness_value
        if happiness_value > happiest_seating:
            happiest_seating_plan: list[tuple, int] = [permutation, happiness_value]
            happiest_seating = happiness_value
    return all_seating_happiness, least_happy_seating_plan, happiest_seating_plan


def get_all_possible_happiness_plans(input_str: str, add_myself: bool = False):
    seating_happiness: list[list[str, str, int]] = extract_seating_happiness(input_str)
    people: list[str] = get_set_of_people(seating_happiness)
    if add_myself:
        seating_happiness = add_myself_to_plans(seating_happiness, people)
    seating_options: dict[str, dict[str, int]] = construct_seating_options(
        seating_happiness
    )
    # print(json.dumps(seating_options, sort_keys=True, indent=4))
    permutations = get_people_permutations(seating_happiness, people)
    (
        all_seating_happiness,
        least_happy_seating_plan,
        happiest_seating_plan,
    ) = get_all_seating_plans(permutations, seating_options)

    result = {
        "all_seating_happiness": all_seating_happiness,
        "least_happy_seating_plan": least_happy_seating_plan,
        "happiest_seating_plan": happiest_seating_plan,
    }
    return result


for example in examples:
    print(example.input_data)
    print(
        example.answer_a,
        get_all_possible_happiness_plans(example.input_data, False).get(
            "happiest_seating_plan"
        )[1],
    )
    print(example.answer_b)
    print()


part_a = get_all_possible_happiness_plans(puzzle.input_data, False).get(
    "happiest_seating_plan"
)[1]
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = get_all_possible_happiness_plans(puzzle.input_data, True).get(
    "happiest_seating_plan"
)[1]
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
