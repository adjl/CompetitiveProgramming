#!/usr/bin/env python3

# LeetCode #637: Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        level = 0
        while queue:
            node, level = queue.pop(0)
            levels[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return [sum(levels[i]) / len(levels[i]) for i in range(1, level + 1)]
