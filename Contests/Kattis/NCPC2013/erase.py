#!/usr/bin/env python3

# Kattis: Erase Securely (erase)
# https://open.kattis.com/problems/erase

n, before, after = int(input()), list(input()), list(input())
if n % 2 == 1:
    for i in range(len(before)):
        before[i] = '0' if before[i] == '1' else '1'
print('Deletion succeeded' if before == after else 'Deletion failed')
