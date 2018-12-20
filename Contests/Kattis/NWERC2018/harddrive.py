#!/usr/bin/env python

# Kattis: Hard Drive (harddrive)
# https://open.kattis.com/problems/harddrive

from collections import deque


def main():
    n, c, _ = [int(i) for i in input().split()]
    broken = list([n + 1 - int(i) for i in input().split()][::-1])
    flipped = {'0': '1', '1': '0'}
    solution = deque(['0'])
    first_bit = '1' if c % 2 == 1 else '0'
    c -= (c % 2)
    # print(broken)

    for size in range(2, n):
        if broken and size == broken[-1]:
            if c > 0 and solution[0] == '1':
                c -= 1
            solution.appendleft('0')
            broken.pop()
            continue
        start_bit = flipped[solution[0]] if c > 0 else solution[0]
        solution.appendleft(start_bit)
        c -= 1
    solution.appendleft(first_bit)
    print(''.join(solution))


if __name__ == '__main__':
    main()
