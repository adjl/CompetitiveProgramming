#!/usr/bin/env python3

# Example: Given a smaller string s and a bigger string b, design an algorithm
# to find all permuta­tions of the shorter string within the longer one. Print
# the location of each permutation.

from collections import Counter
from collections import defaultdict


s, b = set(Counter(input()).items()), input()
n = sum(count for _, count in s)
positions = defaultdict(list)
for i in range(len(b) - n + 1):
    substr = b[i: i + n]
    if s == set(Counter(substr).items()):
        positions[substr].append(i)
for permutation, indices in positions.items():
    print('{}:'.format(permutation), *indices)


# Robin: There is a O(b log s) solution.
