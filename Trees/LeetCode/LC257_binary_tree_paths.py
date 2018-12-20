#!/usr/bin/env python3

# LeetCode #257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        paths = []
        self._binaryTreePaths(root, paths, [])
        return ['->'.join(map(str, path)) for path in paths]

    def _binaryTreePaths(self, root, paths, path):
        if root.left is None and root.right is None:
            paths.append(path + [root.val])
        if root.left is not None:
            self._binaryTreePaths(root.left, paths, path + [root.val])
        if root.right is not None:
            self._binaryTreePaths(root.right, paths, path + [root.val])
