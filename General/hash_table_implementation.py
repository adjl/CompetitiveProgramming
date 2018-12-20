#!/usr/bin/env python3


class Array:

    def __init__(self, max_size, default=lambda: None):
        self.array = [default() for _ in range(max_size)]
        self.max_size = max_size
        self.size = 0

    def __repr__(self):
        return repr(self.array)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.max_size:
            raise IndexError
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.max_size:
            raise IndexError
        if self.array[index] is None or not self.array:
            self.size += 1
        if isinstance(self.array[index], list):
            self.array[index].append(value)
        else:
            self.array[index] = value


class ArrayList:

    def __init__(self, size):
        self.array = Array(size)

    def __repr__(self):
        return repr(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value
        if len(self.array) == self.array.max_size:
            new_array = Array(self.array.max_size * 2)
            for i in range(len(self.array)):
                new_array[i] = self.array[i]
            self.array = new_array


class HashTable:

    def __init__(self, size):
        self.array = Array(size, list)
        self.size = size

    def __repr__(self):
        return repr(self.array)

    def __getitem__(self, key):
        index = self.hash_index(key)
        for k, value in self.array[index]:
            if k == key:
                return value
        return None

    def __setitem__(self, key, value):
        index = self.hash_index(key)
        self.array[index] = value

    def hash_index(self, key):
        def _hash(key):
            key = reversed(list(key))
            hash_sum = 0
            for i, v in enumerate(key):
                hash_sum += ord(v) * 128 ** i
            return hash_sum
        return _hash(key) % self.size
