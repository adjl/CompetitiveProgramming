#!/usr/bin/env python3

# LeetCode #111: Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._minDepth(root, 1)

    def _minDepth(self, root, depth):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return depth
        if root.left is None:
            return self._minDepth(root.right, depth + 1)
        if root.right is None:
            return self._minDepth(root.left, depth + 1)
        left = self._minDepth(root.left, depth + 1)
        right = self._minDepth(root.right, depth + 1)
        return min(left, right)
