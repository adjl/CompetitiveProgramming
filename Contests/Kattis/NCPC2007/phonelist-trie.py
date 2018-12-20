#!/usr/bin/env python3

# Kattis: Phone List (phonelist)
# https://open.kattis.com/problems/phonelist


class Trie:

    def __init__(self):
        self._root = TrieNode('*')

    @property
    def root(self):
        return self._root


class TrieNode:

    def __init__(self, char):
        self._char = char
        self._terminating = False
        self._next = []

    @property
    def char(self):
        return self._char

    @property
    def terminating(self):
        return self._terminating

    @terminating.setter
    def terminating(self, terminating):
        self._terminating = terminating

    def next(self, char):
        for node in self._next:
            if node.char == char:
                return node
        return None

    def add_next(self, node):
        self._next.append(node)
        return node


for _ in range(int(input())):
    trie = Trie()
    consistent = True
    for _ in range(int(input())):
        number = input()
        if not consistent:
            continue
        n = len(number)
        node = trie.root
        for i in range(n):
            char = number[i]
            if node.next(char) is not None:
                node = node.next(char)
                if i == n - 1 and not node.terminating:
                    consistent = False
            elif node.terminating:
                consistent = False
                break
            else:
                node = node.add_next(TrieNode(char))
                if i == n - 1:
                    node.terminating = True
    print('YES' if consistent else 'NO')
