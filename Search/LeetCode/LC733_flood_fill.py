#!/usr/bin/env python3

# LeetCode #733: Flood Fill
# https://leetcode.com/problems/flood-fill/description/


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        s_colour = image[sr][sc]
        to_fill = set()
        queue = [(sr, sc)]
        while queue:
            row, col = queue.pop(0)
            image[row][col] = newColor
            for roff, coff in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
                r, c = row + roff, col + coff
                if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                    continue
                if (r, c) not in to_fill and image[r][c] == s_colour:
                    to_fill.add((r, c))
                    queue.append((r, c))
        return image
