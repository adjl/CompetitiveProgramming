#!/usr/bin/env python3

# Example: Given an array of distinct integer values, count the number of pairs
# of integers that have difference k. For example, given the array
# {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are four pairs with
# difference 2: (1, 3), (3, 5), (5, 7), (7, 9).

from collections import defaultdict


array = [int(i) for i in input().split()]
k = int(input())

possible_pairs = defaultdict(list)
for i in array:
    possible_pairs[i].append(i + k)
    possible_pairs[i].append(i - k)

pairs = set()
for i in array:
    for j in possible_pairs[i]:
        if possible_pairs[j]:
            pairs.add((min(i, j), max(i, j)))

print(*[pair for pair in pairs])
