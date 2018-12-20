#!/usr/bin/env python3

# LeetCode #112: Path Sum
# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# 22


class Solution:
    def hasPathSum(self, root, tree_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self._hasPathSum(root, tree_sum)

    def _hasPathSum(self, root, tree_sum):
        curr_sum = tree_sum - root.val
        if root.left is None and root.right is None:
            return curr_sum == 0
        if root.left is None:
            return self._hasPathSum(root.right, curr_sum)
        if root.right is None:
            return self._hasPathSum(root.left, curr_sum)
        left = self._hasPathSum(root.left, curr_sum)
        right = self._hasPathSum(root.right, curr_sum)
        return left or right
