""" 
Description
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.

Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.

"""

import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def __init__(self):
        self.visited = set()
        self.border = []

    def trapRainWater(self, heights):
        # write your code here
        if not heights or not heights[0]:
            return 0

        m, n = len(heights), len(heights[0])
        self.get_border(heights)
        water = 0
        while self.border:
            if len(self.visited) == m * n:
                break
            h, x, y = heapq.heappop(self.border)
            adj = self.get_unvisited_adj(heights, x, y)
            for (nx, ny) in adj:
                nh = heights[nx][ny]
                if nh > h:
                    self.push(nh, nx, ny)
                else:
                    self.push(h, nx, ny)
                    water += h - nh
        return water

    def get_unvisited_adj(self, heights, x, y):

        h, w = len(heights), len(heights[0])
        adj = []
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in self.visited or nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            adj += [(nx, ny)]
        return adj

    def push(self, h, x, y):
        if (x, y) in self.visited:
            return
        heap_item = (h, x, y)
        heapq.heappush(self.border, heap_item)
        self.visited.add((x, y))

    def get_border(self, heights):
        h, w = len(heights), len(heights[0])

        # left & right borders
        for i in range(h):
            self.push(heights[i][0], i, 0)
            self.push(heights[i][w - 1], i, w - 1)

        # top & bottom borders
        for i in range(w):
            self.push(heights[0][i], 0, i)
            self.push(heights[h - 1][i], h - 1, i)
