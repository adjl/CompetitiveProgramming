#!/usr/bin/env python3

# Kattis: Game Design (gamedesign)
# https://open.kattis.com/problems/gamedesign

import copy

from collections import defaultdict


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_impossible(solution):
    opposite = ''
    if solution[-1] == 'U':
        opposite = 'D'
    elif solution[-1] == 'D':
        opposite = 'U'
    elif solution[-1] == 'L':
        opposite = 'R'
    else:
        opposite = 'L'
    return len(solution) >= 3 and \
        solution[-1] == solution[-3] and solution[-2] == opposite


def main():
    solution = list(input())
    if is_impossible(solution):
        print('impossible')
        return
    coord = Coordinate(0, 0)
    blocks = []
    prev_directions = []
    for i, direction in enumerate(solution):
        dist = 2 * i + 3
        if direction in 'LD':
            dist *= -1
        if direction in 'UD':
            coord.x = dist
            block = copy.copy(coord)
            block.x += 1 if direction == 'U' else -1
        else:
            coord.y = dist
            block = copy.copy(coord)
            block.y += 1 if direction == 'R' else -1
        blocks.append(block)

        if len(prev_directions) == 2 and is_impossible(
                prev_directions + [direction]):
            del blocks[-3]
        prev_directions.append(direction)
        if len(prev_directions) > 2:
            prev_directions.pop(0)

    del blocks[-1]

    print(-coord.y, -coord.x)
    print(len(blocks))
    for block in blocks:
        print(block.y - coord.y, block.x - coord.x)


if __name__ == '__main__':
    main()
