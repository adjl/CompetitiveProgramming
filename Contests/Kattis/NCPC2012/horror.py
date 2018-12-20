#!/usr/bin/env python3

# Kattis: Horror List (horror)
# https://open.kattis.com/problems/horror

from functools import reduce


n, _, l = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]

hi = {}
for movie in h:
    hi[movie] = 0

similarities = []
for _ in range(l):
    a, b = [int(i) for i in input().split()]
    if a in h and b in h:
        continue
    elif a in h:
        hi[b] = 1
    elif b in h:
        hi[a] = 1
    else:
        similarities.append((a, b))

while similarities:
    to_process = []
    for a, b in similarities:
        if a in hi or b in hi:
            to_process.append((a, b))
    if not to_process:
        break
    for a, b in to_process:
        if a in hi and b in hi:
            if hi[a] > hi[b]:
                hi[b] = hi[a] + 1
            elif hi[a] < hi[b]:
                hi[a] = hi[b] + 1
        elif a in hi:
            hi[b] = hi[a] + 1
        elif b in hi:
            hi[a] = hi[b] + 1
        similarities.remove((a, b))

if similarities:
    print(sorted(set(
        reduce(lambda x, y: x + y, [list(s) for s in similarities]))).pop(0))
else:
    print(min([i for i, h in hi.items() if h == max(hi.values())]))
