#!/usr/bin/env python3

import unittest


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root=None):
        self.root = root
        self.output = []

    def traversal_path(self):
        return ' '.join(self.output)

    def preorder_traversal(self):
        self._preorder_traversal(self.root)
        return self.traversal_path()

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        return self.traversal_path()

    def postorder_traversal(self):
        self._postorder_traversal(self.root)
        return self.traversal_path()

    def _preorder_traversal(self, node=None):
        if not node:
            return
        self.output.append(node.data)
        self._preorder_traversal(node.left)
        self._preorder_traversal(node.right)

    def _inorder_traversal(self, node=None):
        if not node:
            return
        self._inorder_traversal(node.left)
        self.output.append(node.data)
        self._inorder_traversal(node.right)

    def _postorder_traversal(self, node=None):
        if not node:
            return
        self._postorder_traversal(node.left)
        self._postorder_traversal(node.right)
        self.output.append(node.data)


class BinaryTreeTraversalTest(unittest.TestCase):

    def setUp(self):
        d = Node('D', Node('H'), Node('I'))
        g = Node('G', right=Node('J'))
        b = Node('B', d, Node('E'))
        c = Node('C', Node('F'), g)
        self.tree = BinaryTree(Node('A', b, c))

    def test_preorder_traversal(self):
        self.assertEqual(self.tree.preorder_traversal(), 'A B D H I E C F G J')

    def test_inorder_traversal(self):
        self.assertEqual(self.tree.inorder_traversal(), 'H D I B E A F C G J')

    def test_postorder_traversal(self):
        self.assertEqual(
            self.tree.postorder_traversal(),
            'H I D E B F J G C A')


if __name__ == '__main__':
    unittest.main()
