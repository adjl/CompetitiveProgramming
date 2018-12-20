#!/usr/bin/env python3

# Example: Print all positive integer solutions to the equation
# a^3 + b^3 = c^3 + d^3 where a, b, c and d are integers between 1 and 1000.

# Can think of equation as a+b == c+d
# Examples: 1+4 == 2+3 ->> 5 == 1+4 == 2+3
# So for sum k, there are >1 integer pairs that add up to it
# We will consider (1+4 == 2+3) !== (2+3 !== 1+4)
#     And for (a,b) == (1,4) !== (4,1)

# Initial idea:
# Loop from i=1 to 1000, taking j=i to 1000 [complexity: O(N^2)]
#     Add (i,j) and (j,i) to sums[k], k = i^3 + j^3
# To prevent repetitive cubing, precomputes all cubes from 1 to 10^3 beforehand [complexity: O(N)]
# For every recorded sum, print all possible combinations of int pairs
#     [suppose longest list of int pairs has size P (P < N), so complexity O(P^2) for each sum]
#     [say there are S sums, so overall complexity is O(S * P^2)]

# How many possible sums could there be?
#     Say you add 1 and 1..1000 ->> there are 1000 sums, ranging from 2..1001
#     Say you add 2 next to 2..1000 ->> sums range from 4..1002, sum range increases by 1
#     Same with 3 and 3..1000, 4, etc...
# Generally, the number of sums from 1 added to 1..N == N sums
#     For every subsequent i=2..N, max possible sum increases by 1 ->> N
#         So starting from i=1 ->> N + N - 1 = 2N - 1
# Complexity: 2N - 1 -> O(2N - 1) == O(2N) == O(N) ->> O(S * P^2) == O(N * P^2)

# Total complexity: O(N^2) + O(N) + O(N * P^2) == O(N^2) + O(N * P^2) == O(N^2)

# Could duplicate pairs possibly be added? No, because the nested looping does not allow that
# e.g., i=1, j=4 but there will never be i=4, j=1 (recall j=i)

from collections import defaultdict


n = 1000

cubes = {}
for i in range(1, n + 1):
    cubes[i] = i ** 3

sums = defaultdict(list)
for i in range(1, n + 1):
    for j in range(i, n + 1):
        sum = cubes[i] + cubes[j]
        sums[sum].append((i, j))
        sums[sum].append((j, i))

for sum, pairs in sums.items():
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            print('k={} a={} b={} c={} d={}'.format(sum, *pairs[i], *pairs[j]))
