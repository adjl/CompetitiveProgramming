#!/usr/bin/env python3

# Kattis: Parking (parking2)
# https://open.kattis.com/problems/parking2

for _ in range(int(input())):
    input()  # Throw away
    x = [int(i) for i in input().split()]
    print((max(x) - min(x)) * 2)
