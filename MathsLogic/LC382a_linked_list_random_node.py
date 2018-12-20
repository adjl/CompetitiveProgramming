#!/usr/bin/env python3

# LeetCode #382: Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

import random


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.vals = []
        self.length = 0
        while head is not None:
            self.vals.append(head.val)
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return self.vals[random.randrange(self.length)]
