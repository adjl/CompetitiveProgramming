#!/usr/bin/env python3


class Heap:

    def __init__(self, heap):
        self.heap = sorted(heap)

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

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, key):
        return self.heap[key]

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

    def add(self, value):
        self.heap.append(value)
        self._bubble_up()

    def extract(self):
        minimum = self.heap[0]
        self._sink_down()
        return minimum


def parent_index(i):
    if i % 2 == 0:
        return i // 2 - 1
    return i // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def main():
    _, k = [int(x) for x in input().split()]
    heap = MinHeap([int(x) for x in input().split()])
    possible = True
    mixes = 0
    while heap[0] < k:
        if len(heap) >= 2:
            heap.add(heap.extract() + 2 * heap.extract())
            mixes += 1
        else:
            possible = False
            break
    print(mixes if possible else -1)


if __name__ == '__main__':
    main()
