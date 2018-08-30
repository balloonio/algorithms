class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        f = [ [0]*n for _ in range(m) ]
        f[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                f[i][j] = math.inf 
                if i-1 >= 0 and i-1 < m:
                    f[i][j] = min(f[i][j], f[i-1][j])
                if j-1 >= 0 and j-1 < n:
                    f[i][j] = min(f[i][j], f[i][j-1])
                f[i][j] = 0 if f[i][j] == math.inf else f[i][j]
                f[i][j] += grid[i][j]
                
        return f[m-1][n-1]