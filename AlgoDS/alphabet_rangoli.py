#!/usr/bin/env python3

import sys


def main():
    message = sys.argv[1]
    length, width = len(message), len(line_pattern(message, 0))
    if length * width > 2000:
        print('Error: Too many characters', file=sys.stderr)
        return
    for i in range(1, length + 1):
        print(line_pattern(message, length - i).center(width, '-'))
    for i in range(length - 1, 0, -1):
        print(line_pattern(message, length - i).center(width, '-'))


def line_pattern(message, offset):
    length = len(message)
    line_pattern = [message[i] for i in range(length - 1, offset, -1)]
    line_pattern += [message[i] for i in range(offset, length)]
    return '-'.join(line_pattern)


if __name__ == '__main__':
    main()
