#!/usr/bin/env python3

# Kattis: Succession (succession)
# https://open.kattis.com/problems/succession

from collections import OrderedDict
from collections import defaultdict


n, m = [int(i) for i in input().split()]
royals = defaultdict(float)
royals[input()] = 1.0

relations = {}
unprocessed = defaultdict(bool)
for _ in range(n):
    child, parent1, parent2 = input().split()
    relations[child] = (parent1, parent2)
    unprocessed[child] = True

generations = OrderedDict()
while relations:
    to_delete = []
    for child, parents in relations.items():
        if not unprocessed[parents[0]] and not unprocessed[parents[1]]:
            generations[child] = parents
            unprocessed[child] = False
            to_delete.append(child)
    for child in to_delete:
        del relations[child]

for child, parent in generations.items():
    royals[child] = (royals[parent[0]] + royals[parent[1]]) / 2.0

claimants = set(input() for _ in range(m))
claimants = sorted(
    [(royal, blood) for royal, blood in royals.items() if royal in claimants],
    key=lambda claimant: claimant[1],
    reverse=True)
print(claimants.pop(0)[0])
