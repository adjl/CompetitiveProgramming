#!/usr/bin/env python3

# LeetCode #841: Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/

from collections import defaultdict


class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        r_table = defaultdict(bool)
        queue = [0]
        while queue:
            room_no = queue.pop(0)
            r_table[room_no] = True
            for key in rooms[room_no]:
                if not r_table[key]:
                    queue.append(key)
        return len(r_table.values()) == len(rooms)
