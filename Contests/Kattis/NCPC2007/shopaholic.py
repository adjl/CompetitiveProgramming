#!/usr/bin/env python3

# Kattis: Shopaholic (shopaholic)
# https://open.kattis.com/problems/shopaholic

input()  # Throw away
p = sorted([int(i) for i in input().split()], reverse=True)
rounds = zip(p[::3], p[1::3], p[2::3])
print(sum([discount for _, _, discount in rounds]))
