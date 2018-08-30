class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not A or not V:
            return 0
        
        n = len(A)
        
        # f[i][j] = the value for first i items with size j 
        f = [ [0]*(m+1) for _ in range(n+1) ]
        
        result = 0
        for i in range(1, n+1):
            for j in range(m+1):
                f[i][j] = max(f[i][j], f[i-1][j])
                f[i][j] = max(f[i][j], f[i-1][j-A[i-1]] + V[i-1]) if j-A[i-1] >= 0 else f[i][j]
        
                if i == n:
                    result = max(result, f[i][j])
                    
        return result