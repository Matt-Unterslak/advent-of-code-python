from typing import List

from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 22

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


class Game:
    player_hp: int
    player_mana: int
    player_armor: int
    boss_hp: int
    boss_dmg: int
    shield_timer: int
    poison_timer: int
    recharge_timer: int
    spells_cast: list
    mana_spent: int

    def __init__(
        self,
        player_hp: int,
        player_mana: int,
        player_armor: int,
        boss_hp: int,
        boss_dmg: int,
        shield_timer: int,
        poison_timer: int,
        recharge_timer: int,
        spells_cast: list[str],
        mana_spent: int,
    ):
        self.player_armor = player_armor
        self.mana_spent = mana_spent
        self.spells_cast = spells_cast
        self.recharge_timer = recharge_timer
        self.poison_timer = poison_timer
        self.shield_timer = shield_timer
        self.boss_dmg = boss_dmg
        self.boss_hp = boss_hp
        self.player_mana = player_mana
        self.player_hp = player_hp

    def _decrease_shield_timer(self):
        if self.shield_timer > 0:
            self.shield_timer -= 1

            if self.shield_timer == 0:
                self.player_armor = 0

    def _decrease_poison_timer(self):
        if self.poison_timer > 0:
            self.boss_hp -= 3
            self.poison_timer -= 1

    def _decrease_recharge_timer(self):
        if self.recharge_timer > 0:
            self.player_mana += 101
            self.recharge_timer -= 1

    def apply_effects(self):
        self._decrease_shield_timer()
        self._decrease_poison_timer()
        self._decrease_recharge_timer()

    def player_turn(self, spell):
        if spell == "magic_missle":
            self.boss_hp -= 4
        elif spell == "drain":
            self.boss_hp -= 2
            self.player_hp += 2
        elif spell == "shield":
            self.shield_timer = 6
            self.player_armor += 7
        elif spell == "poison":
            self.poison_timer = 6
        elif spell == "recharge":
            self.recharge_timer = 5
        self.player_mana -= SPELL_COSTS[spell]

    def boss_turn(self):
        dmg = max(self.boss_dmg - self.player_armor, 1)
        self.player_hp -= dmg

    def add_to_spells_cast(self, spell: str):
        self.spells_cast = list(self.spells_cast) + [spell]

    def add_to_mana_spent(self, spell: str):
        self.mana_spent += SPELL_COSTS[spell]

    def decrease_player_health(self):
        self.player_hp -= 1


initial_game = {
    # player values
    "player_hp": 50,
    "player_mana": 500,
    "player_armor": 0,
    # boss values
    "boss_hp": 0,
    "boss_dmg": 0,
    # effects
    "shield_timer": 0,
    "poison_timer": 0,
    "recharge_timer": 0,
    # player game values
    "spells_cast": [],
    "mana_spent": 0,
}

SPELL_COSTS = {
    "magic_missle": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}


def check_for_endgame(game: Game, min_mana_spent: int):
    if game.boss_hp <= 0:
        min_mana_spent = min(game.mana_spent, min_mana_spent)
        return 1, min_mana_spent
    if game.player_hp <= 0:
        return 2, min_mana_spent
    return 0, min_mana_spent


def try_all_spells(game: Game, min_mana_spent: int, new_games: list):
    castable_spells = [
        spell for spell, cost in SPELL_COSTS.items() if cost <= game.player_mana
    ]
    if game.shield_timer and "shield" in castable_spells:
        castable_spells.remove("shield")
    if game.poison_timer and "poison" in castable_spells:
        castable_spells.remove("poison")
    if game.recharge_timer and "recharge" in castable_spells:
        castable_spells.remove("recharge")

    for spell in castable_spells:
        sub_game: Game = Game(
            player_hp=game.player_hp,
            player_mana=game.player_mana,
            player_armor=game.player_armor,
            boss_hp=game.boss_hp,
            boss_dmg=game.boss_dmg,
            shield_timer=game.shield_timer,
            poison_timer=game.poison_timer,
            recharge_timer=game.recharge_timer,
            spells_cast=game.spells_cast,
            mana_spent=game.mana_spent,
        )
        sub_game.add_to_spells_cast(spell)
        sub_game.add_to_mana_spent(spell)

        # players turn
        sub_game.player_turn(spell)
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        # end early is too much mana spent
        if sub_game.mana_spent > min_mana_spent:
            continue

        # boss's turn
        sub_game.apply_effects()
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        sub_game.boss_turn()
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        new_games.append(sub_game)
    return min_mana_spent


def try_all_games(games: list[Game], min_mana_spent: int, hard_difficulty: bool):
    new_games = []
    for game in games:
        # PART B
        if hard_difficulty:
            game.decrease_player_health()
        endgame, min_mana_spent = check_for_endgame(game, min_mana_spent)
        if endgame:
            continue

        # apply player's turn effects
        game.apply_effects()
        endgame, min_mana_spent = check_for_endgame(game, min_mana_spent)
        if endgame:
            continue

        min_mana_spent = try_all_spells(game, min_mana_spent, new_games)

    return new_games, min_mana_spent


def find_minimal_mana(input_str: str, hard_difficulty: bool = False):
    boss_hp, boss_dmg = [int(x.split(": ")[-1]) for x in input_str.split("\n")]
    game: Game = Game(
        player_hp=50,
        player_mana=500,
        player_armor=0,
        boss_hp=boss_hp,
        boss_dmg=boss_dmg,
        shield_timer=0,
        poison_timer=0,
        recharge_timer=0,
        spells_cast=[],
        mana_spent=0,
    )

    min_mana_spent: int = 9999999
    games: List[game] = [game]
    while len(games):
        games, min_mana_spent = try_all_games(games, min_mana_spent, hard_difficulty)
    return min_mana_spent


print(puzzle.input_data)

part_a = find_minimal_mana(puzzle.input_data, False)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = find_minimal_mana(puzzle.input_data, True)
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
