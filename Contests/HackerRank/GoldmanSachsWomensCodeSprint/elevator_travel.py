#!/usr/bin/env python3

# HackerRank: Elevator Travel
# All Contests > Goldman Sachs Women's CodeSprint > Stock Exchange Matching Algorithm
# https://www.hackerrank.com/contests/goldman-sachs-womens-codesprint/challenges/elevator-travel


def main():
    n = int(input()) + 1
    p = dict(enumerate([0] + [int(i) for i in input().split()]))
    delta_dist = dict(enumerate(
        [abs(p[i] - p[i + 1]) for i in range(len(p) - 1)]))
    min_dist = orig_dist = sum(delta_dist.values())
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            dist = orig_dist - delta_dist[i - 1] - delta_dist[i]
            dist -= delta_dist[j - 1]
            if j < n - 1:
                dist -= delta_dist[j]
            p[i], p[j] = p[j], p[i]
            dist += abs(p[i - 1] - p[i]) + abs(p[i] - p[i + 1])
            dist += abs(p[j - 1] - p[j])
            if j < n - 1:
                dist += abs(p[j] - p[j + 1])
            min_dist = min(dist, min_dist)
            p[i], p[j] = p[j], p[i]
    print(min_dist)


def binary_search(dct, key):
    left, right = 0, len(dct)
    while left < right:
        mid = (left + right) // 2
        if dct[mid] <= key:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    main()
