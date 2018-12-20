#!/usr/bin/env python3


class HashTable:

    def __init__(self):
        self.size = 2048
        self.table = []

    def hash(self, key):
        hash_code = 0  # TODO: Can be improved
        for c in key:
            hash_code = (hash_code * 29 + ord(c)) % self.size
        return hash_code

    def put(self, key, value):
        hash_code = hash(key)
        if self.table[hash_code]:  # Collision
            pass  # TODO: Balanced binary tree, store (key, value)
        else:
            self.table[hash_code] = (key, value)

    def get(self, key):
        hash_code = hash(key)
        if self.table[hash_code]:
            item_key, item_value = self.table[hash_code]
            if key != item_key:
                pass  # Throw HashingError exception
            return item_value
        else:
            pass  # Throw KeyNotFound exception here


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, value, node=None):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(value, node.left)
        elif value >= node.value:
            node.right = self.insert(value, node.right)
            # Haven't done self-balancing binary trees before
            if node.right < node.parent:
                node.parent.parent = node.right
                node.right.right = node.parent
                node.parent = node.right
                node.right.left = node
        return node

    def print(self, node=None):
        if node.left:
            self.print(node.left)
        s = print(node.value, end=' ')
        if node.right:
            self.print(node.right)
        return '{} {}'.format(node.value, s)


def hc(s):
    hash_code = 0
    for i in s:
        hash_code = (hash_code * 29 + ord(i)) % 2048
    return hash_code


def gen_collisions(s):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                word = chr(i + ord('a')) + \
                    chr(j + ord('a')) + chr(k + ord('a'))
                if hc(word) == hc(s):
                    return word


if __name__ == '__main__':
    word = 'txt'
    print('{} {}'.format(gen_collisions(word), hc(word)))
