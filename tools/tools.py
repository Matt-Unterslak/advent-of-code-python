import json

import numpy as np


def create_grid_as_lists(x_size: int, y_size: int) -> list[list[int]]:
    return [[0 for _ in range(y_size)] for _ in range(x_size)]


def create_grid_as_numpy_array(rows: int, columns: int) -> np.ndarray:
    return np.zeros((rows, columns))


def print_grid(grid: list[list[int]], name: str):
    print("__________________")
    print(f"----- {name.title()} Setup ------")
    for row in grid:
        print(row)
    print("__________________")


def print_numpy_array(grid: np.ndarray, name: str):
    print("__________________")
    print(f"----- {name.title()} Setup ------")
    with np.printoptions(edgeitems=30, linewidth=1000):
        for row in grid:
            print(row)
    print("__________________")


def pretty_print_nested_dict(nested_dict: dict):
    print(json.dumps(nested_dict, sort_keys=True, indent=4))
