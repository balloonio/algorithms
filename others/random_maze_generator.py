import random, collections
class Solution:
    """
    start : coordinate (x, y) must be on the border
    end : coordinate (x, y) must be on the border
    board: a 2D board, for simplicity of the problem, lets assure it is a nxn square
    """
    def random_maze(self, start, end, board):
        if not board or not board[0]:
            return
        n = len(board)
        side = n - 1
        queue = collections.deque()
        self.draw_border(start, end, board, queue)
        DIRECTIONS = [(1,0), (0,-1), (-1,0), (0,1)]

        while queue:
            x, y, dir = queue.popleft()
            for delta in range(1, n):
                dx, dy = DIRECTIONS[dir]
                nx, ny = x + dx * delta, y + dy * delta
                if not self.valid_to_wall(nx, ny, board):
                    break
                


    def draw_border(self, start, end, board, queue):
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if (i,j) == start or (i,j) == end:
                    continue
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    board[i][j] = '*'
                    if i == 0:
                        queue.append( (i, j, 0) )
                    elif j == w-1:
                        queue.append( (i, j, 1) )
                    elif i == h-1:
                        queue.append( (i, j, 2) )
                    else:
                        queue.append( (i, j, 3) )

    def test(self, n):
        board = [ [' ']*n for _ in range(n) ]
        start = self.random_on_border(n)
        end = self.random_on_border(n)
        while start == end:
            end = self.random_on_border(n)
        self.random_maze(start, end, board)
        for row in board:
            print(' '.join(row))

    def random_on_border(self, n):
        side = n-1
        idx = random.choice(range(side*4))
        while idx % side == 0:
            idx = random.choice(range(side*4))
        # top
        if idx // side == 0:
            j = idx % side
            return (0, j)
        if idx // side == 1:
            i = idx % side
            return (i, side)
        if idx // side == 2:
            j = side - idx % side
            return (side, j)
        if idx // side == 3:
            i = side - idx % side
            return (i, 0)

sol = Solution()
sol.test(5)
