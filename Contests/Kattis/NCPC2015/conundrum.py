#!/usr/bin/env python3

# Kattis: Cryptographer's Conundrum (conundrum)
# https://open.kattis.com/problems/conundrum

s = input()
n = len(s)
for i in range(n):
    if (s[i] == 'P' and i % 3 == 0 or
            s[i] == 'E' and i % 3 == 1 or
            s[i] == 'R' and i % 3 == 2):
        n -= 1
print(n)
