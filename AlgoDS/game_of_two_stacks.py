#!/usr/bin/env python3

from itertools import accumulate


def main():
    for _ in range(int(input())):
        x = [int(k) for k in input().split()][2]
        a = list(accumulate(int(i) for i in input().split()))
        b = list(accumulate(int(j) for j in input().split()))
        a, b = a[:binary_search(a, x)], b[:binary_search(b, x)]
        max_score = max(len(a), len(b))
        i, j = len(a) - 1, 0
        while i >= 0:
            while j < len(b) and a[i] + b[j] <= x:
                max_score = max(max_score, i + j + 2)
                j += 1
            i -= 1
        print(max_score)


def binary_search(lst, key):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= key:  # The key is lst[mid] *<=* key
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    main()
