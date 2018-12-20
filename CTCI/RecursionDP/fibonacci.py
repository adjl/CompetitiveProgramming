#!/usr/bin/env python3

from collections import defaultdict


def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


def fibonacci(n, memo=defaultdict(int)):
    if n <= 1:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def fib_it_memo(n):
    if n <= 1:
        return n
    memo = defaultdict(int)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_it_var(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c
