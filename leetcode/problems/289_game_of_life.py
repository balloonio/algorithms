# naive solution with O(MN) memory not in place
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        h, w = len(board), len(board[0])
        temp = [[0] * w for _ in range(h)]

        for i in range(h):
            for j in range(w):
                nearby_live = 0
                for nx, ny in self.get_nearby(i, j, board):
                    nearby_live += board[nx][ny]
                if nearby_live < 2 and board[i][j] == 1:
                    temp[i][j] = 0
                elif (nearby_live == 3 or nearby_live == 2) and board[i][j] == 1:
                    temp[i][j] = 1
                elif nearby_live > 3 and board[i][j] == 1:
                    temp[i][j] = 0
                elif nearby_live == 3 and board[i][j] == 0:
                    temp[i][j] = 1

        for i in range(h):
            for j in range(w):
                board[i][j] = temp[i][j]

    def get_nearby(self, i, j, board):
        h, w = len(board), len(board[0])
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            yield nx, ny

# in place solution from leetcode
def gameOfLife(self, board):
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0 or board[i][j] == 2:
                if self.nnb(board, i, j) == 3:
                    board[i][j] = 2
            else:
                if self.nnb(board, i, j) < 2 or self.nnb(board, i, j) > 3:
                    board[i][j] = 3
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2: board[i][j] = 1
            if board[i][j] == 3: board[i][j] = 0


def nnb(self, board, i, j):
    m, n = len(board), len(board[0])
    count = 0
    if i - 1 >= 0 and j - 1 >= 0:   count += board[i - 1][j - 1] % 2
    if i - 1 >= 0:                count += board[i - 1][j] % 2
    if i - 1 >= 0 and j + 1 < n:    count += board[i - 1][j + 1] % 2
    if j - 1 >= 0:                count += board[i][j - 1] % 2
    if j + 1 < n:                 count += board[i][j + 1] % 2
    if i + 1 < m and j - 1 >= 0:    count += board[i + 1][j - 1] % 2
    if i + 1 < m:                 count += board[i + 1][j] % 2
    if i + 1 < m and j + 1 < n:     count += board[i + 1][j + 1] % 2
    return count

# infinite board
def gameOfLifeInfinite(self, live):
    neighbors = collections.Counter()
    for i, j in live:
        for I in (i-1, i, i+1):
            for J in (j-1, j, j+1):
                if I != i or J != j:
                    neighbors[I, J] += 1
    new_live = set()
    for ij in neighbors.keys():
        if neighbors[ij] == 3 or neighbors[ij] == 2 and ij in live:
            new_live.add(ij)
    return new_live