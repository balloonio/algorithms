class Solution:
    """
    @param s: the English word
    @return: The number of keystrokes
    """
    def getAns(self, s):
        # Write your code here
        if not s:
            return 0
            
        n = len(s)
        # f[i][j] = the min stroke to type s[:i] with cap in j state, 0:low 1:UPPER
        f = [ [0]*2 for _ in range(n+1) ]
        f[0][1] = 1 # to enter upper cap 
        
        for i in range(1, n+1):
            if s[i-1].islower():
                f[i][0] = min(f[i-1][0]+1, f[i-1][1]+2)
                f[i][1] = min(f[i-1][0]+2, f[i-1][1]+2)
            else:
                f[i][0] = min(f[i-1][0]+2, f[i-1][1]+2)
                f[i][1] = min(f[i-1][0]+2, f[i-1][1]+1)
                
        return min(f[n])