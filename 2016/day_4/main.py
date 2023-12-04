from typing import List

import numpy as np
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 4

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(char: str, shifts: int):
    current_index = ALPHABET.find(char)

    if current_index + shifts < len(ALPHABET):
        return ALPHABET[current_index + shifts]
    else:
        return ALPHABET[current_index + shifts - len(ALPHABET)]


def decrypt_name(encrypted_name: str, sector_id: int):
    shifts = sector_id % 26
    decrypted_name: str = ""
    for x in encrypted_name:
        if x == "-":
            decrypted_name += " "
        else:
            decrypted_name += shift_letter(x, shifts)
    return decrypted_name


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def get_unique_character_count(encrypted_room_data: list[str]) -> str:
    encrypted_data = "".join([x.lower() for x in encrypted_room_data])
    char_count = {char: 0 for char in list(set(encrypted_data))}
    for char in encrypted_data:
        char_count[char] += 1
    highest_char_first = {
        k: v
        for k, v in sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    }
    values = sorted(list(set([v for v in highest_char_first.values()])), reverse=True)
    chars_sorted_by_occurrence = "".join(
        ["".join(sorted(get_keys_from_value(highest_char_first, v))) for v in values]
    )
    return chars_sorted_by_occurrence


def find_real_rooms(input_str: str):
    data: list[str] = input_str.split("\n")
    real_room_sector_numbers: list[int] = []
    north_pole_sector_id: int = 0
    for room_info in data:
        room_info = room_info.split("-")
        sector_id, checksum = [x.strip("]") for x in room_info[-1].split("[")]
        encrypted_room = room_info[0:-1]

        unique_chars = get_unique_character_count(encrypted_room)

        if unique_chars.startswith(checksum):
            real_room_name: str = decrypt_name("-".join(encrypted_room), int(sector_id))
            if real_room_name.startswith("northpole"):
                north_pole_sector_id = int(sector_id)
            real_room_sector_numbers.append(int(sector_id))

    return sum(real_room_sector_numbers), north_pole_sector_id


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, find_real_rooms(example.input_data)[0])
    print(example.answer_b)
    print()

"""
    Submission A
"""
part_a = find_real_rooms(puzzle.input_data)[0]
print(part_a)
puzzle.answer_a = part_a


"""
    Samples for Part B
"""

samples = ["qzmt-zixmtkozy-ivhz-343"]
for sample in samples:
    print(sample)
    print("very encrypted name", decrypt_name("qzmt-zixmtkozy-ivhz", 343))
    print()

"""
    Submission B
"""
part_b = find_real_rooms(puzzle.input_data)[1]
print(part_b)
puzzle.answer_b = part_b
