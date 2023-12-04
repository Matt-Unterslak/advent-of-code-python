from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 23

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

# Initialize Registers
REGISTERS_A: dict[str, int] = {"a": 0, "b": 0}
REGISTERS_B: dict[str, int] = {"a": 1, "b": 0}


def run_command(command: list[str], command_index, registers: dict[str, int]):
    if command[0] == "hlf":
        registers[command[1]] /= 2
        return command_index + 1
    elif command[0] == "tpl":
        registers[command[1]] *= 3
        return command_index + 1
    elif command[0] == "inc":
        registers[command[1]] += 1
        return command_index + 1
    elif command[0] == "jmp":
        return command_index + int(command[1])
    elif command[0] == "jie":
        if registers[command[1]] % 2 == 0:
            return command_index + int(command[2])
        else:
            return command_index + 1
    elif command[0] == "jio":
        if registers[command[1]] == 1:
            return command_index + int(command[2])
        else:
            return command_index + 1
    return -1


def solve_registers(input_str: str, is_part_1: bool):
    commands = [d.replace(",", "").split(" ") for d in input_str.split("\n")]
    run = 1
    if is_part_1:
        while 0 < run <= len(commands):
            run = run_command(commands[run - 1], run, REGISTERS_A)
        print(REGISTERS_A)
        return REGISTERS_A
    else:
        while 0 < run <= len(commands):
            run = run_command(commands[run - 1], run, REGISTERS_B)
        print(REGISTERS_B)
        return REGISTERS_B


# a_solution = 2
# for example in examples:
#     print(example.input_data)
#     print(a_solution, solve_registers(example.input_data).get("a"))
#     print(example.answer_b)
#     print()


part_a = solve_registers(puzzle.input_data, True).get("b")
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

part_b = solve_registers(puzzle.input_data, False).get("b")
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
