#!/usr/bin/env python3

# Kattis: Card Trick (cardtrick2)
# https://open.kattis.com/problems/cardtrick2

from collections import deque


for _ in range(int(input())):
    n = int(input())
    d = deque([n])
    for i in range(n - 1, 0, -1):
        d.appendleft(i)
        d.rotate(i)
    print(*[i for i in d])
