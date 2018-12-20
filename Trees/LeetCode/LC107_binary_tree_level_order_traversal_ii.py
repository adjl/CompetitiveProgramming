#!/usr/bin/env python3

# LeetCode #107: Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 0)]
        level = 0
        while queue:
            node, level = queue.pop(0)
            levels[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return [levels[i] for i in range(level, -1, -1)]
