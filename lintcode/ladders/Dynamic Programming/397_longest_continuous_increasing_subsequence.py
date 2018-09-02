class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0
            
        # f[i] stands for length of longest asc seq ending in A[i]
        f = [ 1 for _ in range(len(A)) ]
        # f[i] stands for length of longest dsc seq ending in A[i]
        g = [ 1 for _ in range(len(A)) ]
        
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                f[i] = f[i-1] + 1 
            else:
                f[i] = 1 
            if A[i] < A[i-1]:
                g[i] = g[i-1] + 1 
            else:
                g[i] = 1 
        
        maxlen = 1 
        for i in range(len(A)):
            maxlen = max(maxlen, f[i])
            maxlen = max(maxlen, g[i])
        
        return maxlen