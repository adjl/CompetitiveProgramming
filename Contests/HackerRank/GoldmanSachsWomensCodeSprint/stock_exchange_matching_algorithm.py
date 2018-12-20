#!/usr/bin/env python3

# HackerRank: Stock Exchange Matching Algorithm
# All Contests > Goldman Sachs Women's CodeSprint > Stock Exchange Matching Algorithm
# https://www.hackerrank.com/contests/goldman-sachs-womens-codesprint/challenges/stock-exchange-matching-algorithm


def main():
    for _ in range(1):  # range(int(input()))
        input()  # Throwaway
        stocks = [int(s) for s in input().split()]
        prices = [int(p) for p in input().split()]
        exchange = dict(zip(stocks, prices))
        stocks = sorted(stocks)
        for _ in range(int(input())):
            i = binary_search(stocks, int(input()))
            print(exchange[stocks[i]])


def binary_search(lst, key):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= key:
            left = mid + 1
        else:
            right = mid
    return left - 1


if __name__ == '__main__':
    main()
