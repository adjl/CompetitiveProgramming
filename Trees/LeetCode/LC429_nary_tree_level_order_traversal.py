#!/usr/bin/env python

# LeetCode #429: N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import defaultdict


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        level = 0
        while queue:
            node, level = queue.pop(0)
            levels[level].append(node.val)
            queue.extend([(child, level + 1) for child in node.children])
        return [levels[i] for i in range(1, level + 1)]
