#!/usr/bin/env python3

# HackerRank: Elevator Travel
# All Contests > Goldman Sachs Women's CodeSprint > Stock Exchange Matching Algorithm
# https://www.hackerrank.com/contests/goldman-sachs-womens-codesprint/challenges/elevator-travel

from sys import stderr


def main():
    n = int(input()) + 1
    p = [0] + [int(i) for i in input().split()]
    delta_dist = [abs(p[i] - p[i + 1]) for i in range(len(p) - 1)]
    min_dist = orig_dist = sum(delta_dist)
    delta_dist = dict(enumerate(delta_dist))
    for i in range(1, n - 1):
        for j in range(2, n):
            print('i = {}, j = {}'.format(i, j), file=stderr)
            print('lower = {}, upper = {}'.format(p[i], p[j]), file=stderr)
            dist = orig_dist - delta_dist[i - 1] - delta_dist[i]
            print('0: ', dist, delta_dist[i - 1], delta_dist[i], file=stderr)
            dist -= delta_dist[j - 1]
            print('1: ', dist, delta_dist[j - 1], file=stderr)
            if j < n - 1:
                dist -= delta_dist[j]
                print('2: ', dist, delta_dist[j], file=stderr)
            p[i], p[j] = p[j], p[i]
            dist += abs(p[i - 1] - p[i]) + abs(p[i] - p[i + 1])
            print('3: ', dist, abs(p[i - 1] - p[i]),
                  abs(p[i] - p[i + 1]), file=stderr)
            dist += abs(p[j - 1] - p[j])
            print('4: ', dist, abs(p[j - 1] - p[j]), file=stderr)
            if j < n - 1:
                dist += abs(p[j] - p[j + 1])
                print('5: ', dist, abs(p[j] - p[j + 1]), file=stderr)
            min_dist = min(dist, min_dist)
            print('6: ', dist, min_dist, file=stderr)
            p[i], p[j] = p[j], p[i]
    print(min_dist)


if __name__ == '__main__':
    main()
