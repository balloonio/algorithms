class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V or not m:
            return 0

        n = len(A)
        # f[i][j] = max value for first i items with j weight
        f = [[0] * (m + 1) for _ in range(n + 1)]

        result = 0
        for i in range(1, n + 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j]
                f[i][j] = (
                    max(f[i][j], f[i][j - A[i - 1]] + V[i - 1])
                    if j - A[i - 1] >= 0
                    else f[i][j]
                )

                if i == n:
                    result = max(result, f[i][j])

        return result
