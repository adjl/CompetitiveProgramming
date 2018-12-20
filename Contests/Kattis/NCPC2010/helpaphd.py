#!/usr/bin/env python3

# Kattis: Help a PhD Candidate Out! (helpaphd)
# https://open.kattis.com/problems/helpaphd

for _ in range(int(input())):
    n = input()
    if n == 'P=NP':
        print('skipped')
        continue
    print(sum([int(k) for k in n.split('+')]))
