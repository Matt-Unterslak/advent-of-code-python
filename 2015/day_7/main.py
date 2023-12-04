from typing import List, Optional, Union
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 7

AND = " AND "
OR = " OR "
LSHIFT = " LSHIFT "
RSHIFT = " RSHIFT "
NOT = "NOT"
MAX = 65536

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def solve_wire(wire: str, wire_signals: dict[str, Union[int, str]]):
    if wire.isnumeric():
        return int(wire)

    wire_signal = wire_signals[wire]
    if type(wire_signal) is int or wire_signal.isnumeric():
        wire_signals[wire] = int(wire_signal)

    else:
        if AND in wire_signal:
            a, b = wire_signal.split(AND)
            wire_signals[wire] = solve_wire(a, wire_signals) & solve_wire(
                b, wire_signals
            )

        elif OR in wire_signal:
            a, b = wire_signal.split(OR)
            wire_signals[wire] = solve_wire(a, wire_signals) | solve_wire(
                b, wire_signals
            )

        elif LSHIFT in wire_signal:
            a, b = wire_signal.split(LSHIFT)
            wire_signals[wire] = solve_wire(a, wire_signals) << int(b)

        elif RSHIFT in wire_signal:
            a, b = wire_signal.split(RSHIFT)
            wire_signals[wire] = solve_wire(a, wire_signals) >> int(b)

        elif NOT in wire_signal:
            _, a = wire_signal.split()
            wire_signals[wire] = ~(solve_wire(a, wire_signals))
            """
            Tilde (~n) operator is the bitwise negation operator:
            it takes the number n as binary number and “flips” all bits
            e.g. 0 to 1 and 1 to 0 to obtain the complement binary number.
            """

        else:
            wire_signals[wire] = solve_wire(wire_signal, wire_signals)

    return wire_signals[wire]


def process_input(input_str: str) -> tuple[dict[str, Union[int, str]], list[str]]:
    wire_signals: dict[str, Union[int, str]] = {}
    wire_names = []
    for x in input_str.split("\n"):
        signal, wire = x.split(" -> ")
        wire_signals[wire] = signal
        wire_names.append(wire)

    wire_names = list(set(wire_names))
    return wire_signals, wire_names


def solve_input(input_str: str, is_part_1: bool):
    wire_signals, wire_names = process_input(input_str)
    for wire_name in wire_names:
        solve_wire(wire_name, wire_signals)

    if not is_part_1:
        solution_a = wire_signals["a"]
        wire_signals, wire_names = process_input(input_str)
        wire_signals["b"] = solution_a

        for wire_name in wire_names:
            solve_wire(wire_name, wire_signals)

    final_result = {
        k: v if v > 0 else MAX + v
        for k, v in dict(sorted(wire_signals.items())).items()
    }

    return final_result


# for example in examples:
#     print(example.input_data)
#     print(example.answer_a, solve_input(example.input_data))
#     print(example.answer_b)
#     print()

example_input = examples[0].input_data
print(example_input)
print("--------------------")
print(solve_input(example_input, True))


part_a = solve_input(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a.get("a")
print("---------------------")
print()

part_b = solve_input(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b.get("a")
print("---------------------")
print()
