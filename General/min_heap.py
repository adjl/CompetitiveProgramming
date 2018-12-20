#!/usr/bin/env python3

import unittest


class Heap:

    def __init__(self, heap):
        self.heap = heap

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, key):
        if key >= len(self.heap):
            return float('inf')
        return self.heap[key]

    def __setitem__(self, key, value):
        self.heap[key] = value

    def append(self, value):
        self.heap.append(value)

    def pop(self):
        return self.heap.pop()


class MinHeap:

    def __init__(self, heap):
        self.heap = Heap(heap)

    def display(self):
        return self.heap.heap

    def add(self, x):
        self.heap.append(x)
        self._bubble_up()

    def extract(self):
        minimum = self.heap[0]
        self._sink_down()
        return minimum

    def _bubble_up(self):
        node = len(self.heap) - 1
        parent = parent_index(node)
        while node >= 0 and parent >= 0 and self.heap[node] < self.heap[parent]:
            self.heap[node], self.heap[parent] = self.heap[parent], self.heap[node]
            node = parent
            parent = parent_index(node)

    def _sink_down(self):
        if len(self.heap) == 1:
            self.heap.pop()
            return
        node = 0
        self.heap[node] = self.heap.pop()
        left, right = left_child(node), right_child(node)
        while self.heap[node] > min(self.heap[left], self.heap[right]):
            if self.heap[left] < self.heap[right]:
                self.heap[node], self.heap[left] = self.heap[left], self.heap[node]
                node = left
            else:
                self.heap[node], self.heap[right] = self.heap[right], self.heap[node]
                node = right
            left, right = left_child(node), right_child(node)


def parent_index(i):
    if i % 2 == 0:
        return i // 2 - 1
    return i // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


class MinHeapTest(unittest.TestCase):

    def testAdd(self):
        heap = MinHeap([1, 3, 5])
        heap.add(6)
        self.assertEqual(heap.display(), [1, 3, 5, 6])
        heap.add(2)
        self.assertEqual(heap.display(), [1, 2, 5, 6, 3])
        heap.add(4)
        self.assertEqual(heap.display(), [1, 2, 4, 6, 3, 5])
        heap.add(0)
        self.assertEqual(heap.display(), [0, 2, 1, 6, 3, 5, 4])
        heap.add(7)
        self.assertEqual(heap.display(), [0, 2, 1, 6, 3, 5, 4, 7])

    def testExtract(self):
        heap = MinHeap([0, 2, 1, 6, 3, 5, 4, 7])
        self.assertEqual(heap.extract(), 0)
        self.assertEqual(heap.display(), [1, 2, 4, 6, 3, 5, 7])
        self.assertEqual(heap.extract(), 1)
        self.assertEqual(heap.display(), [2, 3, 4, 6, 7, 5])
        self.assertEqual(heap.extract(), 2)
        self.assertEqual(heap.display(), [3, 5, 4, 6, 7])
        self.assertEqual(heap.extract(), 3)
        self.assertEqual(heap.display(), [4, 5, 7, 6])
        self.assertEqual(heap.extract(), 4)
        self.assertEqual(heap.display(), [5, 6, 7])
        self.assertEqual(heap.extract(), 5)
        self.assertEqual(heap.display(), [6, 7])
        self.assertEqual(heap.extract(), 6)
        self.assertEqual(heap.display(), [7])
        self.assertEqual(heap.extract(), 7)
        self.assertEqual(heap.display(), [])


if __name__ == '__main__':
    unittest.main()
