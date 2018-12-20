#!/usr/bin/env python3

# LeetCode #382: Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/description/

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
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        chosen, node, n = None, self.head, 0
        while node is not None:
            n += 1
            if random.randrange(n) == 0:
                chosen = node
            node = node.next
        return chosen.val
