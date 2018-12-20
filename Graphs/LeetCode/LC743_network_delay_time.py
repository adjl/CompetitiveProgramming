#!/usr/bin/env python3

# LeetCode #743: Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/

import sys

from collections import defaultdict


class Node:
    def __init__(self):
        self.min_time = sys.maxsize
        self.inbound = {}
        self.outbound = {}


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        nodes = defaultdict(lambda: None)
        for u, v, w in times:
            if nodes[u] is None:
                nodes[u] = Node()
            if nodes[v] is None:
                nodes[v] = Node()
            nodes[u].outbound[v] = w
            nodes[v].inbound[u] = w

        signalled = defaultdict(bool)
        nodes[K].min_time = 0
        queue = [K]

        while queue:
            node_id = queue.pop(0)
            signalled[node_id] = True
            node = nodes[node_id]
            if node.inbound:
                node.min_time = min(node.inbound.values())
            for out in node.outbound:
                if not signalled[out]:
                    nodes[out].inbound[node_id] += node.min_time
                    queue.append(out)
        if len(signalled) < N:
            return -1
        return max(node.min_time for node in nodes.values())
