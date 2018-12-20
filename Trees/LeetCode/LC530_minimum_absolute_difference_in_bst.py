#!/usr/bin/env python3

# LeetCode #530: Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        seq = self.getSequence(root)
        min_diff = sys.maxsize
        for i in range(len(seq) - 1):
            min_diff = min(min_diff, abs(seq[i] - seq[i + 1]))
        return min_diff

    def getSequence(self, root):
        if root is None:
            return []
        seq = []
        seq.extend(self.getSequence(root.left))
        seq.append(root.val)
        seq.extend(self.getSequence(root.right))
        return seq
