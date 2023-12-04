import copy
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 18

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def extract_state_from_input(input_str: str) -> list[list[int]]:
    rows = []
    for x in input_str.split("\n"):
        rows.append([int(y.replace(".", "0").replace("#", "1")) for y in x])
    return rows


def get_lights_surrounding(
    light_x: int, light_y: int, setup: list[list[int]]
) -> list[int]:
    lights: list[int] = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            light_wanted_x = light_x + r
            light_wanted_y = light_y + c
            if 0 <= light_wanted_x < len(setup) and 0 <= light_wanted_y < len(setup[0]):
                if (light_wanted_x, light_wanted_y) != (light_x, light_y):
                    lights.append(setup[light_wanted_x][light_wanted_y])
    return lights


def update_light_state(
    light_x: int,
    light_y: int,
    current_value: int,
    surrounding_lights: list[int],
    final_state: list[list[int]],
):
    if current_value == 1:
        if sum(surrounding_lights) in [2, 3]:
            final_state[light_x][light_y] = 1
        else:
            final_state[light_x][light_y] = 0
    else:
        if sum(surrounding_lights) == 3:
            final_state[light_x][light_y] = 1
        else:
            final_state[light_x][light_y] = 0
    return final_state


def calculate_next_light_step(
    input_setup: list[list[int]], corners_on: bool
) -> list[list[int]]:
    final_setup = copy.deepcopy(input_setup)

    for r in range(len(final_setup)):
        for c in range(len(final_setup[0])):
            # print("------------- Light Loop --------------")
            # print(r, c, final_setup[r][c])
            lights: list[int] = get_lights_surrounding(r, c, input_setup)
            # print(lights)
            final_setup = update_light_state(
                r, c, final_setup[r][c], lights, final_setup
            )
            if corners_on:
                for x, y in [
                    (0, 0),
                    (0, len(final_setup[0]) - 1),
                    (len(final_setup) - 1, 0),
                    (len(final_setup) - 1, len(final_setup[0]) - 1),
                ]:
                    final_setup[x][y] = 1

    return final_setup


def solve_lights_on(input_str: str, number_of_steps: int, corners_on: bool = False):
    initial_setup: list[list[int]] = extract_state_from_input(input_str)

    final_setup: list[list[int]] = copy.deepcopy(initial_setup)
    for i in range(number_of_steps):
        final_setup: list[list[int]] = calculate_next_light_step(
            final_setup, corners_on
        )

    total_lights_on = sum([y for x in final_setup for y in x])
    return total_lights_on


for example in examples:
    print(example.input_data)
    print()
    print(example.answer_a, solve_lights_on(example.input_data, 4))
    print(example.answer_b, solve_lights_on(example.input_data, 4, True))
    print()
    break


part_a = solve_lights_on(puzzle.input_data, 100)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = solve_lights_on(puzzle.input_data, 100, True)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
