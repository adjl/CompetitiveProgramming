#!/usr/bin/env python3

# Kattis: Train Passengers (trainpassengers)
# https://open.kattis.com/problems/trainpassengers

c, n = [int(i) for i in input().split()]
train = 0
possible = True
for stop in range(n):
    left, entered, waited = [int(i) for i in input().split()]
    if stop == 0 and left > 0:
        possible = False
        break
    elif stop == n - 1 and (train - left != 0 or entered > 0 or waited > 0):
        possible = False
        break
    train = train + entered - left
    if not 0 <= train <= c or (c - train > 0 and waited > 0):
        possible = False
        break
print('possible' if possible else 'impossible')
