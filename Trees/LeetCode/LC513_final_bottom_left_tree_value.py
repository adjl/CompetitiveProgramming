#!/usr/bin/env python3

# LeetCode #513: Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        queue = [(root, 1)]
        last_level, left_val = 0, None
        while queue:
            node, level = queue.pop(0)
            if level > last_level:
                last_level, left_val = level, node.val
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return left_val
