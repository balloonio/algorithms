"""
给定一个二维矩阵 其中只包含0或1
如果某个1它的同一行或者同一列里还有其他的1 那么我们可以把这个1挖掉
请问最多可以挖多少个1
"""

import heapq, random


class Solution:
    """
    board: list[ list[int] ]
    @return : int
    """

    def dig_most_ones(self, board):
        if not board or not board[0]:
            return 0

        # split 1s into 3 categories
        # I. this 1 has other 1s in either its column or its row, but not both
        # II. this 1 has other 1s in both its column and its row
        # III. this 1 has other 1s in neither its column nor its row

        oneheap = []

        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item == 1:
                    category = self.categorize_one_at(i, j, board)
                    thisone = [category, i, j]
                    heapq.heappush(oneheap, thisone)
        maxdig = 0
        while oneheap and oneheap[0][0] != 3:
            category, i, j = heapq.heappop(oneheap)
            print("dig 1 at ({0}, {1})".format(i, j))
            board[i][j] = 0
            for row in board:
                print(row)
            maxdig += 1
            # update status for the rest of the 1s
            for one in oneheap:
                if one[1] != i and one[2] != j:
                    continue
                one[0] = self.categorize_one_at(one[1], one[2], board)
            heapq.heapify(oneheap)
        return maxdig

    def categorize_one_at(self, i, j, board):
        row1s = sum(board[i])
        col1s = 0
        for row in board:
            col1s += row[j]

        if row1s == 1 and col1s == 1:
            return 3
        if row1s == 1 or col1s == 1:
            return 1
        return 2


sol = Solution()
h, w = 30, 50
board = [[0] * w for _ in range(h)]
origones = 0
for i in range(h):
    for j in range(w):
        board[i][j] = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        origones += board[i][j]
    print(board[i])
print(sol.dig_most_ones(board))
print(origones)

"""
original board:
[1, 0, 1, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 1, 1, 0]
dig 1 at (0, 0)
[0, 0, 1, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 1, 1, 0]
dig 1 at (0, 2)
[0, 0, 0, 0, 1, 1, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 1, 1, 0]
dig 1 at (0, 4)
[0, 0, 0, 0, 0, 1, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 1, 1, 0]
dig 1 at (0, 5)
[0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 1, 1, 0]
dig 1 at (4, 4)
[0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (1, 0)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (1, 3)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (1, 6)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (3, 3)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 0, 0, 0, 1]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (3, 6)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (2, 0)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (3, 0)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (3, 2)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 0]
dig 1 at (4, 2)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
dig 1 at (2, 1)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
dig 1 at (2, 5)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0]
dig 1 at (4, 1)
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0]
17
"""
