#!/usr/bin/env python3

# LeetCode #589: N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class MyIterativeSolution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            values.append(node.val)
            stack.extend(reversed(node.children))
        return values


class MyRecursiveSolution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self._preorder(root, [])

    def _preorder(self, root, values):
        if root is None:
            return []
        values.append(root.val)
        for child in root.children:
            self._preorder(child, values)
        return values
