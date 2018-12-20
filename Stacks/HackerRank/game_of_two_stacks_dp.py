#!/usr/bin/env python3

# HackerRank: Game of Two Stacks
# Practice > Data Structures > Stacks
# https://www.hackerrank.com/challenges/game-of-two-stacks/problem

from itertools import accumulate


def main():
    for _ in range(int(input())):
        _, _, x = [int(k) for k in input().split()]
        a = list(accumulate([int(i) for i in input().split()]))
        b = list(accumulate([int(j) for j in input().split()]))
        max_score = 0
        i = binary_search(a, x)  # Blah
        while i >= 0 and a[i] > x:
            i -= 1
        while i >= 0:
            j = binary_search(b, x - a[i])
            while j >= 0 and b[j] > x - a[i]:
                j -= 1
            if j >= 0 and a[i] + b[j] <= x:
                score = i + j + 2
                if score > max_score:
                    max_score = score
            elif a[i] <= x:
                score = i + 1
                if score > max_score:
                    max_score = score
            i -= 1
        j = binary_search(b, x)
        while j >= 0 and b[j] > x:
            j -= 1
        if j >= 0 and b[j] <= x:
            score = j + 1
            if score > max_score:
                max_score = score
        print(max_score)


def binary_search(lst, key):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    main()
