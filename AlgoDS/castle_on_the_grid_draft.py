#!/usr/bin/env python3

from sys import stderr


def main():
    for t in range(int(input())):
        grid = [input() for _ in range(int(input()))]
        start_x, start_y, goal_x, goal_y = [int(x) for x in input().split()]
        expected_result = True if input() == 'True' else False
        print('Displaying grid...', file=stderr)
        for line in grid:
            print(''.join(line), file=stderr)
        path = {}
        if grid[start_x][start_y] == 'X' or grid[goal_x][goal_y] == 'X':
            print('Invalid start or goal coordinates', file=stderr)
            has_path = False
        else:
            has_path, path = bfs(
                grid, (start_x, start_y), (goal_x, goal_y))
        path = get_path_lst(path, (start_x, start_y))
        turns = get_num_turns(path)
        print('{}: {} -> Path({}): {}'.format(
            t, 'PASS' if expected_result == has_path else 'FAIL',
            turns, '->'.join(str(node) for node in path)))
        print('-' * 40, file=stderr)


def get_path_lst(path, start):
    path_lst = [start]
    src = start
    while src in path:
        dest = path[src]
        path_lst.append(dest)
        src = dest
    return path_lst


def get_num_turns(path):
    turns = 0
    last_change = None
    for i in range(len(path) - 1):
        (prev_x, prev_y), (pos_x, pos_y) = path[i], path[i + 1]
        if last_change is None:
            last_change = 'fst' if prev_x != pos_x else 'snd'
            turns += 1
        if prev_x != pos_x and last_change == 'snd':
            last_change = 'fst'
            turns += 1
        elif prev_y != pos_y and last_change == 'fst':
            last_change = 'snd'
            turns += 1
    return turns


def bfs(grid, start, goal):
    start_x, start_y = start
    edges = [(None, start)]
    print('DEBUG; {}'.format(edges), file=stderr)
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    print('Start ({},{})'.format(*start), file=stderr)
    visited[start_x][start_y] = True
    backtrack = []
    while edges:
        print('Displaying visited graph...', file=stderr)
        for line in visited:
            print(line, file=stderr)
        prev, pos = edges.pop(0)
        backtrack.append((prev, pos))
        print('Current position: ({},{})'.format(*pos), file=stderr)
        if pos == goal:
            print('Current position ({},{}) is goal!'.format(*pos),
                  file=stderr)
            print('Backtrack: {}'.format(backtrack), file=stderr)
            return True, get_path(backtrack)
        neighbour_nodes = get_neighbours(grid, visited, *pos)
        neighbour_edges = [(pos, neighbour_node) for neighbour_node
                           in neighbour_nodes]
        print('Neighbours of ({},{}) are:'.format(*pos), file=stderr)
        for edge in neighbour_edges:
            print(edge, file=stderr)
        edges.extend(neighbour_edges)
    return False, []


def get_neighbours(grid, visited, pos_x, pos_y):
    neighbours = []
    for offset_x, offset_y in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
        x, y = pos_x + offset_x, pos_y + offset_y
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
            continue
        print('Checking if ({},{}) is a path'.format(x, y), file=stderr)
        if grid[x][y] == '.' and not visited[x][y]:
            print('Adding ({},{}) as path'.format(x, y), file=stderr)
            neighbours.append((x, y))
            visited[x][y] = True
    return neighbours


def get_path(backtrack):
    prev, pos = backtrack.pop()
    path = {prev: pos}
    while backtrack:
        prev, pos = backtrack.pop()
        if pos in path:
            path[prev] = pos
    print('Path: {}'.format(path), file=stderr)
    return path


# I find it easier to just push edges. Here's how I do the backtracking:

# for edge in edges[node]:
#     if node not in path:
#         path[edge] = node
#         edges.push(edge)

# So I do the "processing" of a node and its incoming edge at the time
# when I'm adding it to the edges


if __name__ == '__main__':
    main()
