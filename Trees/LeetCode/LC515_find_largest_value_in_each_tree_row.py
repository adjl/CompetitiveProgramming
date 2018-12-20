#!/usr/bin/env python3

# LeetCode #515: Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        values = defaultdict(list)
        queue = [(root, 1)]
        level = 0
        while queue:
            node, level = queue.pop(0)
            values[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return [max(values[i]) for i in range(1, level + 1)]
