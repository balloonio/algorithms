class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if not A:
            return 0

        all = sum(A)
        if m >= all:
            return all

        n = len(A)
        # f[i][j] = with first i items given, the weight j is possible to be constructed
        f = [False]*(m+1)
        f[0] = True

        max_weight = 0
        for i in range(1, n+1):
            for j in reversed(range(m+1)):
                f[j] = True if (j-A[i-1] >= 0 and f[j-A[i-1]]) or f[j] else False
                max_weight = max(max_weight, j) if f[j] else max_weight

        return max_weight