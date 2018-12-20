#!/usr/bin/env python3

# HackerRank: Designer Doormat
# Practice > Python > Strings
# https://www.hackerrank.com/challenges/designer-door-mat/problem

import sys


def main():
    n = int(input('Enter height of doormat (must be odd): '))
    if n % 2 == 0:
        print('Number must be odd', file=sys.stderr)
        return
    m = n * 3
    for i in range(1, (n // 2) + 1):
        print(line_pattern(m, i))
    print('Welcome to /r/Christianity - Please leave your bigotry by the door'.center(m, '-'))
    for i in range(n // 2, 0, -1):
        print(line_pattern(m, i))


def line_pattern(m, i):
    length = i * 2 - 1
    return '{0}{1}{0}'.format('-' * ((m - length * 3) // 2), '.|.' * length)


if __name__ == '__main__':
    main()
