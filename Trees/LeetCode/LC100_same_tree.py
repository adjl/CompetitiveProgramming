#!/usr/bin/env python3

# LeetCode #100: Same Tree
# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if (p is None) ^ (q is None):
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return p.val == q.val and left and right
