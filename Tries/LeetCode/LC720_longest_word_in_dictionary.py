#!/usr/bin/env python3

# LeetCode #720: Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/description/

from collections import defaultdict
from copy import copy


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        words = sorted(words)
        groups = defaultdict(list)
        char = ''
        for word in words:
            if word[0] != char:
                char = word[0]
            groups[char].append(list(word))
        longest_word = []
        for char in groups:
            char_group = groups[char]
            prefix = char_group[0]
            skip_prefix = False
            if len(char_group) == 1 and not longest_word:
                longest_word = copy(prefix)
                continue
            for i in range(1, len(char_group)):
                word, j = char_group[i], 0
                for j in range(len(prefix)):
                    if prefix[j] != word[j]:
                        if len(prefix) > len(longest_word) and \
                                (not longest_word or prefix < longest_word):
                            longest_word = copy(word)
                        prefix[j] = word[j]
                        skip_prefix = True
                        break
                prefix.extend(word[j + 1:])
            if skip_prefix:
                continue
            if len(prefix) > len(longest_word) and \
                    (not longest_word or prefix < longest_word):
                longest_word = copy(word)
        return ''.join(longest_word)
