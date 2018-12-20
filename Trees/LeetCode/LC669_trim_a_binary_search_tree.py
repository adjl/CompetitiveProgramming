#!/usr/bin/env python3

# LeetCode #669: Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left = left
            root.right = right
            return root
        return left if left is not None else right
