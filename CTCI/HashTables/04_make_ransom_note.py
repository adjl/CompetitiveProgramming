#!/usr/bin/env python3

# Example: A ransom note can be formed by cutting words out of a magazine to
# form a new sentence. How would you figure out if a ransom note (represented
# as a string) can be formed from a given magazine (string)?

# Use a counter. Ransom note length N, magazine length M.
# Complexity: O(N) + O(M) + O(N) = O(2N + M) = O(N + M)

import sys

from collections import Counter


def count_words(s):
    return Counter(s.split())


note = count_words(input())
magazine = count_words(input())
for word in note:
    if note[word] > magazine[word]:
        print(False)
        sys.exit()
print(True)
