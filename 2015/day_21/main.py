import itertools
from collections import namedtuple
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 21

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

PLAYER_MAX_HITPOINTS = 100
Item = namedtuple("Item", ["name", "cost", "dmg", "armor"])

WEAPONS = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]
ARMOR = [
    Item("Nothing", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

RINGS = [
    Item("Nothing 1", 0, 0, 0),
    Item("Nothing 2", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
]


def calculate_player_dmg_armor_cost(
    weapon: Item, armor: Item, ring_1: Item, ring_2: Item
) -> tuple[int, int, int]:
    player_dmg = weapon.dmg + ring_1.dmg + ring_2.dmg
    player_armor = armor.armor + ring_1.armor + ring_2.armor
    cost = weapon.cost + armor.cost + ring_1.cost + ring_2.cost
    return player_dmg, player_armor, cost


def does_player_win(
    player_hitpoints: int,
    player_dmg: int,
    player_armor: int,
    boss_hitpoints: int,
    boss_dmg: int,
    boss_armor: int,
):
    boss_loss_per_turn = player_dmg - boss_armor
    if boss_loss_per_turn < 1:
        boss_loss_per_turn = 1
    player_loss_per_turn = boss_dmg - player_armor
    if player_loss_per_turn < 1:
        player_loss_per_turn = 1

    # the player goes first and gets n+1 turns
    n, remain = divmod(boss_hitpoints, boss_loss_per_turn)
    if remain == 0:
        n -= 1
    if player_loss_per_turn * n >= player_hitpoints:
        return False
    return True


def calculate_minimum_spent_to_win(input_str: str):
    boss_hitpoints, boss_damage, boss_armor = [
        int(x.split(": ")[-1]) for x in input_str.split("\n")
    ]
    ring_options = list(itertools.combinations(RINGS, 2))

    min_cost = 9999
    max_cost = 0
    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring_1, ring_2 in ring_options:
                player_dmg, player_armor, cost = calculate_player_dmg_armor_cost(
                    weapon, armor, ring_1, ring_2
                )
                if does_player_win(
                    PLAYER_MAX_HITPOINTS,
                    player_dmg,
                    player_armor,
                    boss_hitpoints,
                    boss_damage,
                    boss_armor,
                ):
                    # lowest cost items to win
                    min_cost = min(cost, min_cost)
                else:
                    # highest cost items and still lose
                    max_cost = max(cost, max_cost)
    return min_cost, max_cost


print(puzzle.input_data)
min_cost, max_cost = calculate_minimum_spent_to_win(puzzle.input_data)


part_a = min_cost
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = max_cost
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
