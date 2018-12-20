#!/usr/bin/env python3

# LeetCode #938: Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0
        range_sum = root.val if L <= root.val <= R else 0
        if root.val > L:
            range_sum += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            range_sum += self.rangeSumBST(root.right, L, R)
        return range_sum
