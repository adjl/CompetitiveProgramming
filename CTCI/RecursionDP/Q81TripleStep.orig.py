#!/usr/bin/env python3

# 8.1 Triple Step: A child is running up a staircase with n steps and can hop
# either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how
# many possible ways the child can run up the stairs.
# Hints: #152, #178, #217, #237, #262, #359
# Solution: p. 353

from collections import defaultdict


def count_ways_recur(n):
    if n < 0:
        return 0
    if 0 <= n <= 1:
        return 1
    return (count_ways_recur(n - 1) +
            count_ways_recur(n - 2) +
            count_ways_recur(n - 3))


def count_ways(n, memo=defaultdict(int)):
    if n < 0:
        return 0
    if 0 <= n <= 1:
        return 1
    if memo[n] == 0:
        memo[n] = (count_ways(n - 1, memo) +
                   count_ways(n - 2, memo) +
                   count_ways(n - 3, memo))
    return memo[n]


def count_ways_it_memo(n):
    memo = defaultdict(int)
    memo[0], memo[1] = 1, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]


def count_ways_it_var(n):
    if 0 <= n <= 1:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(2, n + 1):
        ways = a + b + c
        a, b, c = b, c, ways
    return ways
