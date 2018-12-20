#!/usr/bin/env python3

# 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of
# grid with r rows and c columns. The robot can only move in two directions,
# right and down, but certain cells are "off limits" such that the robot cannot
# step on them. Design an algorithm to find a path for the robot from the top
# left to the bottom right.
# Hints: #331, #360, #388
# Solution: p. 344

from collections import defaultdict
from timeit import timeit

from gridQ82 import grid


def count_paths_recur(grid, row=0, col=0):
    if (row >= grid.num_rows or col >= grid.num_cols or
            grid.grid[row][col] is None):
        return 0
    if row == grid.num_rows - 1 and col == grid.num_cols - 1:
        return 1
    return (count_paths_recur(grid, row + 1, col) +
            count_paths_recur(grid, row, col + 1))


def count_paths(grid, row=0, col=0, memo=defaultdict(lambda: None)):
    if (row >= grid.num_rows or col >= grid.num_cols or
            grid.grid[row][col] is None):
        return 0
    if row == grid.num_rows - 1 and col == grid.num_cols - 1:
        return 1
    if memo[row, col] is None:
        memo[row, col] = (count_paths(grid, row + 1, col) +
                          count_paths(grid, row, col + 1))
    return memo[row, col]


def count_paths_it(grid):
    paths = [[0 for _ in range(grid.num_cols)] for _ in range(grid.num_rows)]
    for row in range(grid.num_rows - 1, -1, -1):
        for col in range(grid.num_cols - 1, -1, -1):
            if row == grid.num_rows - 1 and col == grid.num_cols - 1:
                paths[row][col] = 1
            elif grid.grid[row][col] is None:
                paths[row][col] = 0
            elif row == grid.num_rows - 1:
                paths[row][col] = paths[row][col + 1]
            elif col == grid.num_cols - 1:
                paths[row][col] = paths[row + 1][col]
            else:
                paths[row][col] = paths[row + 1][col] + paths[row][col + 1]
    return paths[0][0]


def find_path_recur(grid):
    path = []
    if _find_path_recur(grid, grid.num_rows - 1, grid.num_cols - 1, path):
        return path
    return None


def _find_path_recur(grid, row, col, path):
    if row < 0 or col < 0 or grid.grid[row][col] is None:
        return False
    if ((row, col) == (0, 0) or
            _find_path_recur(grid, row - 1, col, path) or
            _find_path_recur(grid, row, col - 1, path)):
        path.append((row, col))
        return True
    return False


def find_path(grid):
    path = []
    if _find_path(grid, grid.num_rows - 1, grid.num_cols - 1, path, set()):
        return path
    return None


def _find_path(grid, row, col, path, blocks):
    if (row < 0 or col < 0 or
            grid.grid[row][col] is None or (row, col) in blocks):
        return False
    if ((row, col) == (0, 0) or
            _find_path(grid, row - 1, col, path, blocks) or
            _find_path(grid, row, col - 1, path, blocks)):
        path.append((row, col))
        return True
    blocks.add((row, col))
    return False


def time(cmd):
    return timeit(cmd, number=100000, globals=globals())
