#!/usr/bin/env python3

# 8.3 Magic Index: A magic index in an array A[0...n-1] is defined to be an
# index such that A[i] = i. Given a sorted array of distinct integers, write a
# method to find a magic index, if one exists, in array A.
# Follow up: What if the values are not distinct?
# Hints: #170, #204, #240, #286, #340
# Solution: p. 346


def magic_index_search(a, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if a[mid] == mid:
        return mid
    left = magic_index_search(a, low, min(mid - 1, a[mid]))
    if left is not None:
        return left
    return magic_index_search(a, max(mid + 1, a[mid]), high)


a = [int(i) for i in input().split()]
print(magic_index_search(a, 0, len(a) - 1))
