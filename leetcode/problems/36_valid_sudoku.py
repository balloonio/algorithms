class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if not board or not board[0]:
            return False

        return self.row_valid(board) and self.col_valid(board) and self.box_valid(board)

    def row_valid(self, board):
        visited = set()
        for row in board:
            visited.clear()
            for num in row:
                if num in visited and num != ".":
                    return False
                visited.add(num)
        return True

    def col_valid(self, board):
        h, w = len(board), len(board[0])
        visited = set()
        for j in range(w):
            visited.clear()
            for i in range(h):
                if board[i][j] in visited and board[i][j] != ".":
                    return False
                visited.add(board[i][j])
        return True

    def box_valid(self, board):
        visited = set()
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                visited.clear()
                for i in range(9):
                    dx, dy = i // 3, i % 3
                    if (
                        board[x + dx][y + dy] in visited
                        and board[x + dx][y + dy] != "."
                    ):
                        return False
                    visited.add(board[dx + x][dy + y])
        return True
