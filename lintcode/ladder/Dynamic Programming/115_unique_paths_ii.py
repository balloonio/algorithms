class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        rowlen = len(obstacleGrid)
        collen = len(obstacleGrid[0])
        
        f = [ [0]*collen for _ in range(2) ]
        f[0][0] = 1 if obstacleGrid[0][0] !=1 else 0
        now, old = 1, 0
        for row in range(rowlen):
            now, old = old, now
            f[now] = f[now] if row == 0 else [0]*collen
            for col in range(collen):
                if obstacleGrid[row][col] == 1:
                    f[now][col] = 0
                    continue
                
                if row-1 >= 0 and row-1 < rowlen:
                    f[now][col] += f[old][col]
                if col-1 >= 0 and col-1 < collen:
                    f[now][col] += f[now][col-1]
            print(f)    
        return f[now][collen-1]