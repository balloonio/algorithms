class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        if not word:
            return True

        visited = set()
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                visited.add( (i,j) )
                found = self.helper(board, i, j, word, 0, visited)
                visited.remove( (i,j) )
                if found:
                    return True
        return False

    def helper(self, board, i, j, word, widx, visited):
        if board[i][j] != word[widx]:
            return False
        if widx == len(word) - 1:
            return True

        for (ni, nj) in self.get_nearby_unvisited(board, i, j, visited):
            visited.add( (ni,nj) )
            found = self.helper(board, ni, nj, word, widx+1, visited)
            visited.remove( (ni, nj) )
            if found:
                return True
        return False

    def get_nearby_unvisited(self, board, i, j, visited):
        h, w = len(board), len(board[0])
        result = []
        for (di, dj) in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i + di,  j+ dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if (ni, nj) in visited:
                continue
            result.append( (ni, nj) )
        return result

# be careful with edge case where board has only one letter
# in that case L30-L35 has no coordinate to explore thus return False
