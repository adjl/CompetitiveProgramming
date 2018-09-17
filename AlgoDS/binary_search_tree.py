#!/usr/bin/env python3

import copy
import unittest


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root
        self._traversal = []
        self._init(self.root)

    def _init(self, current_node, parent=None):
        if not current_node:
            return
        current_node.parent = parent
        self._init(current_node.left, current_node)
        self._init(current_node.right, current_node)

    def traverse(self, get_data=lambda x: x.data):
        self._traversal = []
        self._inorder_traversal(self.root, get_data)
        return ' '.join(map(str, self._traversal))

    def lookup(self, data):
        return self._lookup(data, self.root)

    def insert(self, new_node):
        self._insert(new_node, self.root)

    def max(self, current_node=None):
        if current_node:
            return self._max(current_node)
        return self._max(self.root)

    def min(self, current_node=None):
        if current_node:
            return self._min(current_node)
        return self._min(self.root)

    def delete(self, data):
        node_to_delete = self.lookup(data)
        if not node_to_delete:
            return None
        parent = node_to_delete.parent
        if node_to_delete.left and node_to_delete.right:
            min_right = self._min(node_to_delete.right)
            self.delete(min_right.data)
            orig_node = copy.copy(node_to_delete)
            node_to_delete.data = min_right.data
            return orig_node
        if node_to_delete.left:
            parent.left = node_to_delete.left
        elif node_to_delete.right:
            parent.right = node_to_delete.right
        elif parent.left is node_to_delete:
            parent.left = None
        else:
            parent.right = None
        return node_to_delete

    def _lookup(self, data, current_node):
        if not current_node:
            return None
        if data == current_node.data:
            return current_node
        if data < current_node.data:
            return self._lookup(data, current_node.left)
        return self._lookup(data, current_node.right)

    def _insert(self, new_node, current_node):
        if not current_node:
            return new_node
        if new_node.data < current_node.data:
            current_node.left = self._insert(new_node, current_node.left)
        else:
            current_node.right = self._insert(new_node, current_node.right)
        return current_node

    def _inorder_traversal(self, current_node, get_data):
        if not current_node:
            return
        self._inorder_traversal(current_node.left, get_data)
        self._traversal.append(get_data(current_node))
        self._inorder_traversal(current_node.right, get_data)

    def _max(self, current_node):
        if not current_node:
            return None
        if not current_node.right:
            return current_node
        return self._max(current_node.right)

    def _min(self, current_node):
        if not current_node:
            return None
        if not current_node.left:
            return current_node
        return self._min(current_node.left)


class BinarySearchTreeTest(unittest.TestCase):

    def setUp(self):
        two = Node(2, Node(1), Node(3))
        four = Node(4, two, Node(5))
        eight = Node(8, Node(7), Node(9))
        self.tree = BinarySearchTree(Node(6, four, eight))

    def test_InitTree(self):
        def get_data(current_node):
            if not current_node.parent:
                return None
            return current_node.parent.data
        self.assertEqual(self.tree.traverse(get_data), '2 4 2 6 4 None 8 6 8')

    def testInsert_LeftChild(self):
        two = Node(2, Node(1), Node(3))
        four = Node(4, two, Node(5))
        eight = Node(8, right=Node(9))
        self.tree = BinarySearchTree(Node(6, four, eight))
        self.tree.insert(Node(7))
        self.assertEqual(self.tree.traverse(), '1 2 3 4 5 6 7 8 9')

    def testInsert_RightChild(self):
        two = Node(2, Node(1))
        four = Node(4, two, Node(5))
        eight = Node(8, Node(7), Node(9))
        self.tree = BinarySearchTree(Node(6, four, eight))
        self.tree.insert(Node(3))
        self.assertEqual(self.tree.traverse(), '1 2 3 4 5 6 7 8 9')

    def testLookup_None(self):
        self.assertIsNone(self.tree.lookup(0))

    def testLookup_WithData(self):
        self.assertIsNotNone(self.tree.lookup(5))

    def testDelete_None(self):
        self.assertIsNone(self.tree.delete(0))

    def testDelete_NoChildren(self):
        self.assertIsNotNone(self.tree.delete(3))
        self.assertEqual(self.tree.traverse(), '1 2 4 5 6 7 8 9')

    def testDelete_LeftChild(self):
        self.assertIsNotNone(self.tree.delete(7))
        self.assertEqual(self.tree.traverse(), '1 2 3 4 5 6 8 9')

    def testDelete_RightChild(self):
        self.assertIsNotNone(self.tree.delete(9))
        self.assertEqual(self.tree.traverse(), '1 2 3 4 5 6 7 8')

    def testDelete_TwoChildren(self):
        deleted_node = self.tree.delete(6)
        self.assertIsNotNone(deleted_node)
        self.assertEqual(deleted_node.data, 6)
        self.assertEqual(self.tree.traverse(), '1 2 3 4 5 7 8 9')

    def testMax_None(self):
        self.tree = BinarySearchTree()
        self.assertIsNone(self.tree.max())

    def testMax_WithData(self):
        self.assertEqual(self.tree.max().data, 9)

    def testMin_None(self):
        self.tree = BinarySearchTree()
        self.assertIsNone(self.tree.min())

    def testMin_WithData(self):
        self.assertEqual(self.tree.min().data, 1)


# Try Robin's suggestion:
# "if you want to naturally extend it you could then go on to create a
# balanced binary tree from a list and re-traverse it to get the list back out"

# Try Robin's tip:
# "A handy trick is to shuffle the value in a node down to the bottom and then
# delete the node it ends up in
# This means fewer cases to think about"

# def reassign_child(self, old_child, new_child):
#   if self.right_child is old_child:
#     self.right_child = new_child
#   elif self.left_child is old_child:
#     self.left_child = new_child
#   else:
#     throw FaultyAssumptionException()

# TODO:
# 1) Do not return nodes for insert() and delete()
# 2) _init() and on the fly node parent/rank initialisation
# 3) Redo delete()
# 4) Time complexity review


if __name__ == '__main__':
    unittest.main()
