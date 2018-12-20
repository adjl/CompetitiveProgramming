#!/usr/bin/env python3

# Kattis: Planting Trees (plantingtrees)
# https://open.kattis.com/problems/plantingtrees

input()  # Throw away
seedlings = sorted([int(i) for i in input().split()], reverse=True)
print(max([i + s for i, s in enumerate(seedlings)]) + 2)
