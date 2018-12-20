#!/usr/bin/env python

# LeetCode #559: Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if not root.children:
            return 1
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1


class MySolution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self._maxDepth(root, 1)

    def _maxDepth(self, root, depth):
        if root is None:
            return depth - 1
        max_depth = depth
        for child in root.children:
            max_depth = max(max_depth, self._maxDepth(child, depth + 1))
        return max_depth
