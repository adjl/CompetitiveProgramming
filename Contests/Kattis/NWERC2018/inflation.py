#!/usr/bin/env python3

# Kattis: Inflation (inflation)
# https://open.kattis.com/problems/inflation

import sys


def main():
    n = int(input())
    balloons = [i for i in range(1, n + 1)]
    canisters = sorted([int(i) for i in input().split()])
    min_fraction = sys.maxsize
    for i in range(n):
        if canisters[i] > balloons[i]:
            print('impossible')
            return
        min_fraction = min(min_fraction, canisters[i] / balloons[i])
    print(min_fraction)


if __name__ == '__main__':
    main()
