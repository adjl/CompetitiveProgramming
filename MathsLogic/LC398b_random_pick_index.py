#!/usr/bin/env python3

# LeetCode #398: Random Pick Index
# https://leetcode.com/problems/random-pick-index/description/

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        chosen, target_count = 0, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                target_count += 1
                if random.randrange(target_count) == 0:
                    chosen = i
        return chosen
