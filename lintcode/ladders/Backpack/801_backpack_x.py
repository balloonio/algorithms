class Solution:
    def backPackX(self, n):
        # write your code here
        if n <= 0 :
            return  0

        COSTS = [150, 250, 350]
        SIZE = 3
        f = [[False]*(n+1) for _ in range(SIZE+1)]
        f[0][0] = True

        result = n
        for i in range(1, SIZE+1):
            for j in range(n+1):
                f[i][j] |= f[i-1][j]
                f[i][j] |= f[i][j-COSTS[i-1]] if j-COSTS[i-1] >= 0 else False

                if i == SIZE:
                    result = min(result, n-j) if f[i][j] else result

        return result