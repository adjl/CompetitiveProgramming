#!/usr/bin/env python3

# LeetCode #872: Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = self.getLeafSequence(root1)
        seq2 = self.getLeafSequence(root2)
        return seq1 == seq2

    def getLeafSequence(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        seq = self.getLeafSequence(root.left)
        seq.extend(self.getLeafSequence(root.right))
        return seq
