#!/usr/bin/env python

# LeetCode #590: N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class MyIterativeSolution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, values = [root], []
        processed = set()
        while stack:
            node = stack[-1]
            if node not in processed and node.children:
                stack.extend(node.children[::-1])
                processed.add(node)
            else:
                node = stack.pop()
                values.append(node.val)
                processed.discard(node)
        return values


class MyRecursiveSolution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self._postorder(root, [])

    def _postorder(self, root, values):
        if root is None:
            return []
        values = []
        for child in root.children:
            values.extend(self._postorder(child, values))
        values.append(root.val)
        return values
