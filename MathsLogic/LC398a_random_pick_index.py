#!/usr/bin/env python3

# LeetCode #398: Random Pick Index
# https://leetcode.com/problems/random-pick-index/description/

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

import random

from collections import defaultdict


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_table = defaultdict(list)
        for i in range(len(nums)):
            self.nums_table[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.nums_table[target])
