#!/usr/bin/env python3

# Kattis: Timebomb (timebomb)
# https://open.kattis.com/problems/timebomb

import sys


def get_digit(display, index):
    digit = [[display[i][index + j] for j in range(3)] for i in range(5)]
    digit = '\n'.join([''.join(line) for line in digit])
    return codes[digit]


codes = {
    '***\n* *\n* *\n* *\n***': 0,
    '  *\n  *\n  *\n  *\n  *': 1,
    '***\n  *\n***\n*  \n***': 2,
    '***\n  *\n***\n  *\n***': 3,
    '* *\n* *\n***\n  *\n  *': 4,
    '***\n*  \n***\n  *\n***': 5,
    '***\n*  \n***\n* *\n***': 6,
    '***\n  *\n  *\n  *\n  *': 7,
    '***\n* *\n***\n* *\n***': 8,
    '***\n* *\n***\n  *\n***': 9
}


display = [input() for _ in range(5)]
num_digits = (len(display[0]) + 1) // 4 - 1
total, index = 0, 0
while num_digits >= 0:
    try:
        total += get_digit(display, index) * (10 ** num_digits)
    except KeyError:
        print('BOOM!!')
        sys.exit()
    index += 4
    num_digits -= 1
print('BEER!!' if total % 6 == 0 else 'BOOM!!')
