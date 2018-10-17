#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/castle-on-the-grid/problem

inc_coord_funcs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)]


def main():
    n = int(input())
    grid = [input() for _ in range(n)]
    start_x, start_y, goal_x, goal_y = [int(x) for x in input().split()]
    all_turns = turns_bfs(n, grid, start_x, start_y)
    path_turns = [turns for pos, turns in all_turns if pos == (goal_x, goal_y)]
    print(min(path_turns))


def turns_bfs(n, grid, start_x, start_y):
    edges = [(None, (start_x, start_y), None, 1)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_x][start_y] = False
    turns = []
    while edges:
        edge = edges.pop(0)
        turns.append((edge[1], edge[3]))
        edges.extend(get_neighbours(n, grid, visited, edge))
    return turns


def get_neighbours(n, grid, visited, edge):
    prev_pos, orig_pos, curr_dir, turns = edge
    neighbours = []
    for inc_coord in inc_coord_funcs:
        curr_pos = orig_pos
        while True:
            x, y = inc_coord(*curr_pos)
            if (x < 0 or x >= n) or (y < 0 or y >= n) or grid[x][y] == 'X':
                break
            if grid[x][y] == '.' and not visited[x][y]:
                if prev_pos is None:
                    curr_dir = 'x' if curr_pos[0] != x else 'y'
                edge = (curr_pos, (x, y), curr_dir, turns)
                neighbours.append((curr_pos, (x, y), *update_dir_turns(*edge)))
                visited[x][y] = True
            curr_pos = x, y
    return neighbours


def update_dir_turns(prev_pos, curr_pos, curr_dir, turns):
    (prev_x, prev_y), (curr_x, curr_y) = prev_pos, curr_pos
    if prev_x != curr_x and curr_dir == 'y':
        curr_dir = 'x'
        turns += 1
    elif prev_y != curr_y and curr_dir == 'x':
        curr_dir = 'y'
        turns += 1
    return curr_dir, turns


if __name__ == '__main__':
    main()
