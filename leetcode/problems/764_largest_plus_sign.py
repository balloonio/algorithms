class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if not N:
            return 0
        
        up = [ [0]*N for _ in range(N)]
        dn = [ [0]*N for _ in range(N)]
        lf = [ [0]*N for _ in range(N)]
        rt = [ [0]*N for _ in range(N)]
        
        mine_set = set()
        for m in mines:
            mine_set.add( (m[0], m[1]) )
        
        for i in range(N):
            for j in range(N):
                up[i][j] = 0 if (i,j) in mine_set else (1 if i-1 < 0 else up[i-1][j] + 1)
                lf[i][j] = 0 if (i,j) in mine_set else (1 if j-1 < 0 else lf[i][j-1] + 1)
        
        for i in reversed(range(N)):
            for j in reversed(range(N)):
                dn[i][j] = 0 if (i,j) in mine_set else (1 if i+1 >= N else dn[i+1][j] + 1)
                rt[i][j] = 0 if (i,j) in mine_set else (1 if j+1 >= N else rt[i][j+1] + 1)
        result = 0        
        for i in range(N):
            for j in range(N):
                result = max(result, min(up[i][j], dn[i][j], lf[i][j], rt[i][j]) )
        return result

# L22 L23 L27 L28 Remember to +1 from the previous dp, and also +1 if no previous dp