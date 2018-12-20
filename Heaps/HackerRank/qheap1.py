#!/usr/bin/env python3

# HackerRank: QHEAP1
# Practice > Data Structures > Heap
# https://www.hackerrank.com/challenges/qheap1/problem


class Heap:

    def __init__(self):
        self.heap = []

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

    def __init__(self):
        self.heap = Heap()

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

    def peek(self):
        return self.heap[0]


def parent_index(i):
    if i % 2 == 0:
        return i // 2 - 1
    return i // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def main():
    heap = MinHeap()
    to_delete = []
    for _ in range(int(input())):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            heap.add(query[1])
        elif query[0] == 2:
            to_delete.append(query[1])
        else:
            while heap.peek() in to_delete:
                to_delete.remove(heap.extract())
            print(heap.peek())


if __name__ == '__main__':
    main()
