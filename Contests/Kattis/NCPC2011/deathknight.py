#!/usr/bin/env python3

# Kattis: Death Knight Hero (deathknight)
# https://open.kattis.com/problems/deathknight

wins = 0
for _ in range(int(input())):
    if input().find('CD') == -1:
        wins += 1
print(wins)
