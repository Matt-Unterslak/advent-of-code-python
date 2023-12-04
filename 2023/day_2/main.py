from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 2

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def sum_ids_of_games(input_str: str):
    print()
    combination = {"red": 12, "green": 13, "blue": 14}
    possible_games: list[int] = []
    game_powers: list[int] = []
    for game_info in input_str.split("\n"):
        game_min_balls: dict = {"red": 0, "green": 0, "blue": 0}
        # print(f"{game_info=}")
        game, random_cubes = game_info.split(": ")
        game_id: int = int(game.split()[1])
        random_cubes = [x.split(",") for x in random_cubes.split(";")]
        # print(f"{game=}")
        # print(f"{random_cubes=}")
        random_draws = [y.split() for x in random_cubes for y in x]
        # print(f"{random_draws=}")
        possible_game: bool = True
        for random_draw in random_draws:
            if possible_game and int(random_draw[0]) > combination[random_draw[1]]:
                possible_game = False

            if int(random_draw[0]) > game_min_balls[random_draw[1]]:
                game_min_balls[random_draw[1]] = int(random_draw[0])

        game_powers.append(
            game_min_balls["red"] * game_min_balls["green"] * game_min_balls["blue"]
        )

        if possible_game:
            possible_games.append(game_id)

        # print("-" * 80)
        # print()

    # print(f"{game_powers=}")
    # print(f"{possible_games=}")
    return sum(possible_games), sum(game_powers)


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, sum_ids_of_games(example.input_data)[0])
    print(example.answer_b, sum_ids_of_games(example.input_data)[1])
    print()

"""
    Submission A
"""
# print(puzzle.input_data)
puzzles_solutions = sum_ids_of_games(puzzle.input_data)
part_a = puzzles_solutions[0]
print(part_a)
puzzle.answer_a = part_a


"""
    Submission B
"""
part_b = puzzles_solutions[1]
print(part_b)
puzzle.answer_b = part_b
