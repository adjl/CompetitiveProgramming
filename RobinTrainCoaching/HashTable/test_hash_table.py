#!/usr/bin/env python3

import unittest

from hash_table import BinaryTree
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def testPutGet(self):
        self.hash_table.put('August', 8)
        self.assertEqual(self.hash_table.get('August'), 8)

    def testRaiseKeyError(self):
        with self.assertRaises(KeyError):
            self.hash_table.get('May')

    def testRaiseHashingError(self):
        self.hash_table.table[800] = ('aju', 13)
        with self.assertRaises(KeyError):
            self.hash_table.get('txt')


class TestBalancingTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def testInsert(self):
        self.tree.insert(1)
        self.assertEqual(self.tree.print(), '1')
        self.tree.insert(2)
        self.assertEqual(self.tree.print(), '1 2')
        self.tree.insert(5)
        self.assertEqual(self.tree.print(), '1 2 5')
        self.tree.insert(3)
        self.assertEqual(self.tree.print(), '1 2 3 5')
        self.tree.insert(4)
        self.assertEqual(self.tree.print(), '1 2 3 4 5')


if __name__ == '__main__':
    unittest.main()
