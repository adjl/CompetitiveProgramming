#!/usr/bin/env python3

# Kattis: ls (ls)
# https://open.kattis.com/problems/ls

import re


pattern = input()
for p, r in [('.', r'\.')]:
    pattern = re.sub(p, r, pattern)
pattern = ''.join(['[', pattern, '$]'])
for _ in range(int(input())):
    filename = input()
    if re.search(pattern, filename) is not None:
        print(filename)
