class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0

        pathsTo = [[0] * n for _ in range(m)]
        pathsTo[0][0] = 1

        print(pathsTo)

        for row in range(m):
            for col in range(n):
                if row != 0:
                    pathsTo[row][col] += pathsTo[row - 1][col]
                if col != 0:
                    pathsTo[row][col] += pathsTo[row][col - 1]
                # print(pathsTo)
        return pathsTo[m - 1][n - 1]
