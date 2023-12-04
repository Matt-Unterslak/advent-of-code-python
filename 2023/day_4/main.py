from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 4

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def find_winning_cards(input_str: str):
    print()
    cards = input_str.split("\n")
    winning_scores = []
    winning_cards = {}
    for card in cards:
        card_number, card_numbers = [x for x in card.split(": ")]
        card_number = int(card_number.split()[1])
        winning_numbers, card_numbers = card_numbers.split(" | ")
        card_numbers = card_numbers.split()
        winning_numbers = winning_numbers.split()
        card_winning_numbers = [x for x in card_numbers if x in winning_numbers]
        winning_score = 0
        for i, _ in enumerate(card_winning_numbers):
            if winning_score == 0:
                winning_score = 1
            else:
                winning_score *= 2
        winning_scores.append(winning_score)
    return sum(winning_scores)


def process_cards(cards: list[str]) -> tuple[dict[int, list[int]], dict[int, int]]:
    card_results: dict[int, list[int]] = {}
    winning_result: dict[int, int] = {}
    for card in cards:
        card_number, card_numbers = [x for x in card.split(": ")]
        card_number = int(card_number.split()[1])
        winning_numbers, card_numbers = card_numbers.split(" | ")
        card_numbers = card_numbers.split()
        winning_numbers = winning_numbers.split()
        card_winning_numbers = [x for x in card_numbers if x in winning_numbers]
        additional_scratch_cards = [
            card_number + i + 1 for i in range(len(card_winning_numbers))
        ]
        card_results[card_number] = additional_scratch_cards
        winning_result[card_number] = 1
    return card_results, winning_result


def count_total_scratch_cards(input_str: str):
    # print()
    cards: list[str] = input_str.split("\n")
    card_win_results, winning_cards = process_cards(cards)
    highest_card = max(winning_cards.keys())
    # print(f"{highest_card=}")
    for current_card in range(1, highest_card + 1):
        for _ in range(winning_cards[current_card]):
            cards_won = card_win_results[current_card]
            # print(f"{cards_won=}")
            for card in cards_won:
                winning_cards[card] += 1
        # print(f"{winning_cards=}")

    total_scratch_cards = sum([v for _, v in winning_cards.items()])
    # print(f"{total_scratch_cards=}")
    return total_scratch_cards


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, find_winning_cards(example.input_data))
    print(example.answer_b, count_total_scratch_cards(example.input_data))
    print()

"""
    Submission A
"""
part_a = find_winning_cards(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = count_total_scratch_cards(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
