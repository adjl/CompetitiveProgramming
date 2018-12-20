#!/usr/bin/env python3

# LeetCode #703: Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq as hq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = sorted(nums)
        self.k = k
        while len(self.heap) > k:
            hq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            hq.heappush(self.heap, val)
        elif val > self.heap[0]:
            hq.heappushpop(self.heap, val)
        return self.heap[0]
