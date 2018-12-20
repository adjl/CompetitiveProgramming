#!/usr/bin/ev python3

# LeetCode #897: Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        seq = self.getSequence(root)
        for i in range(len(seq) - 1):
            seq[i].left = None
            seq[i].right = seq[i + 1]
        seq[-1].left = seq[-1].right = None
        return seq.pop(0)

    def getSequence(self, root):
        if root is None:
            return []
        seq = []
        seq.extend(self.getSequence(root.left))
        seq.append(root)
        seq.extend(self.getSequence(root.right))
        return seq
