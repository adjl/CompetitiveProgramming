#!/usr/bin/env python3

# LeetCode #110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self._isBalanced(root.left)
        right = self._isBalanced(root.right)
        return left and right

    def _isBalanced(self, root):
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 1
        left = self._isBalanced(root.left) + 1
        right = self._isBalanced(root.right) + 1
        return 0 <= abs(left - right) <= 1
