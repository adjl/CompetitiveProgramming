from collections import namedtuple


num_rows, num_cols = 8, 8
grid_map = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

off_limits = [(1, 2), (1, 6), (2, 4), (3, 0), (3, 2), (3, 5),
              (4, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 5)]

for off_limit in off_limits:
    row, col = off_limit
    grid_map[row][col] = None

Grid = namedtuple('Grid', ['grid', 'num_rows', 'num_cols'])
grid = Grid(grid_map, num_rows, num_cols)
