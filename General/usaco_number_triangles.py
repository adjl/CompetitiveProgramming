#!/usr/bin/env python3

# USACO Number Triangle
# https://pastebin.com/vnvjJQYx
# https://stackoverflow.com/questions/16750470/usaco-number-triangle

from collections import defaultdict


def main():
    r = int(input())
    triangle = [[int(i) for i in input().split()] for _ in range(r)]
    sums = [defaultdict(int) for _ in range(r + 1)]
    for row in range(r - 1, -1, -1):
        for i, num in enumerate(triangle[row]):
            # print('hello')
            sums[row][i] = max(sums[row + 1][i], sums[row + 1][i + 1]) + num
    print(sums[0][0])


if __name__ == '__main__':
    main()
