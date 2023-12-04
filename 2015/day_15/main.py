import re
from functools import partial
from typing import List
from aocd.models import Puzzle

from tools.input_processor import process_input_multiline

YEAR: int = 2015
DAY: int = 15

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

MAX_TEASPOONS: int = 100


def mixtures(n: int, total: int):
    if n == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


def get_score(spoons, ingredients, restrict_calories=False) -> int:
    n_items = len(spoons)

    if restrict_calories:
        calorie_count = 0
        for ingredient in range(n_items):
            calorie_count += spoons[ingredient] * ingredients[ingredient][4]
        if calorie_count != 500:
            return 0

    total_score = 1
    for prop in range(4):
        score = 0
        for ingredient in range(n_items):
            score += spoons[ingredient] * ingredients[ingredient][prop]
        score = max(score, 0)
        total_score *= score
    return total_score


def part1(ingredients: List[List[int]]) -> int:
    max_score = 0
    n_ingredients = len(ingredients)
    for mixture in mixtures(n_ingredients, 100):
        max_score = max(max_score, get_score(mixture, ingredients))
    return max_score


def part2(ingredients: List[List[int]]) -> int:
    max_score = 0
    n_ingredients = len(ingredients)
    for mixture in mixtures(n_ingredients, 100):
        max_score = max(max_score, get_score(mixture, ingredients, True))
    return max_score


def calculate_recipes(input_str: str, is_part_1: bool):
    ingredients = []
    for item in process_input_multiline(input_str):
        name, characteristics = item.split(":")
        ingredients.append([int(x) for x in re.findall(r"-?\d+", characteristics)])
    if is_part_1:
        max_score = part1(ingredients)
    else:
        max_score = part2(ingredients)
    return max_score


for example in examples:
    print(example.input_data)
    print(example.answer_a, calculate_recipes(example.input_data, True))
    print(example.answer_b)
    print()

part_a = calculate_recipes(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()
print()

part_b = calculate_recipes(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
