import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 14

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def extract_reindeer_race_metrics(reindeer_strs: str) -> dict[str, dict[str, int]]:
    reindeer_metrics: dict[str, dict[str, int]] = {}
    for reindeer_str in reindeer_strs.split("\n"):
        name = reindeer_str.split()[0]
        speed_str = reindeer_str.split(",")[0]
        speed = int(re.findall(r"-?\d+", speed_str.split(" km/s ")[0])[0])
        speed_time = int(re.findall(r"-?\d+", speed_str.split(" km/s ")[1])[0])

        rest_str = reindeer_str.split(",")[1]
        rest_time = int(re.findall(r"-?\d+", rest_str.split("seconds")[0])[0])

        reindeer_metrics[name] = {
            "speed": speed,
            "speed_time": speed_time,
            "rest_time": rest_time,
        }
    return reindeer_metrics


def calculate_movement_for_seconds(
    reindeer: str,
    seconds: int,
    speed_time: int,
    speed: int,
    rest_time: int,
    reindeer_distance: dict[str, int],
) -> dict[str, int]:
    if seconds <= 0:
        return reindeer_distance
    else:
        if seconds >= speed_time:
            distance = speed_time * speed
            seconds -= speed_time
        else:
            distance = seconds * speed
            seconds -= seconds

        reindeer_distance[reindeer] += distance

        seconds -= rest_time
        calculate_movement_for_seconds(
            reindeer, seconds, speed_time, speed, rest_time, reindeer_distance
        )
        return reindeer_distance


def calculate_reindeer_movement(
    seconds: int, reindeer_metrics: dict[str, dict[str, int]]
):
    reindeer_distance: dict[str, int] = {
        reindeer: 0 for reindeer, metrics in reindeer_metrics.items()
    }
    for reindeer, metrics in reindeer_metrics.items():
        speed = metrics.get("speed")
        speed_time = metrics.get("speed_time")
        rest_time = metrics.get("rest_time")

        reindeer_distance = calculate_movement_for_seconds(
            reindeer, seconds, speed_time, speed, rest_time, reindeer_distance
        )
    return reindeer_distance


def get_longest_distance(
    reindeer_distance: dict[str, int]
) -> dict[str, tuple[str, int]]:
    longest_distance = 0
    longest_distance_tuple: tuple[str, int] = tuple()

    for reindeer, distance in reindeer_distance.items():
        if distance > longest_distance:
            longest_distance_tuple = (reindeer, distance)
            longest_distance = distance
    results: dict[str, tuple[str, int]] = {"longest_distance": longest_distance_tuple}
    return results


def get_highest_score(reindeer_scores: dict[str, int]) -> dict[str, tuple[str, int]]:
    highest_score = 0
    highest_score_tuple: tuple[str, int] = tuple()

    for reindeer, score in reindeer_scores.items():
        if score > highest_score:
            highest_score_tuple = (reindeer, score)
            highest_score = score
    results: dict[str, tuple[str, int]] = {"highest_score": highest_score_tuple}
    return results


def assign_winning_scores(
    reindeer_distance: dict[str, int], reindeer_scores: dict[str, int]
) -> dict[str, int]:
    current_winner: tuple[str, int] = get_longest_distance(reindeer_distance).get(
        "longest_distance"
    )
    reindeer_scores[current_winner[0]] += 1

    return reindeer_scores


def calculate_distance_after_n_seconds(
    input_str: str, seconds: int
) -> dict[str, tuple[str, int]]:
    reindeer_metrics: dict[str, dict[str, int]] = extract_reindeer_race_metrics(
        input_str
    )
    # print(reindeer_metrics)
    reindeer_scores: dict[str, int] = {name: 0 for name in reindeer_metrics.keys()}

    for i in range(seconds):
        reindeer_distance: dict[str, int] = calculate_reindeer_movement(
            i + 1, reindeer_metrics
        )
        reindeer_scores: dict[str, int] = assign_winning_scores(
            reindeer_distance, reindeer_scores
        )
    print(seconds, reindeer_distance, reindeer_scores)
    race_results_distance = get_longest_distance(reindeer_distance)
    race_results_scores = get_highest_score(reindeer_scores)
    return race_results_distance | race_results_scores


for example in examples:
    print(example.input_data)
    print(
        example.answer_a,
        calculate_distance_after_n_seconds(example.input_data, 1),
        calculate_distance_after_n_seconds(example.input_data, 10),
        calculate_distance_after_n_seconds(example.input_data, 11),
        calculate_distance_after_n_seconds(example.input_data, 12),
        calculate_distance_after_n_seconds(example.input_data, 138),
        calculate_distance_after_n_seconds(example.input_data, 174),
        calculate_distance_after_n_seconds(example.input_data, 1000),
        calculate_distance_after_n_seconds(example.input_data, 2503),
    )
    print(example.answer_b)
    print()


part_a = calculate_distance_after_n_seconds(puzzle.input_data, 2503).get(
    "longest_distance"
)[1]
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = calculate_distance_after_n_seconds(puzzle.input_data, 2503).get(
    "highest_score"
)[1]
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
