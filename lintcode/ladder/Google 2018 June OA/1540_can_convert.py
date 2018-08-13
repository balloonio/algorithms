""" 
Description
Given two string S and T, determine if S can be changed to T by deleting some letters (including 0 letter)

Have you met this question in a real interview?  
Example
input:
S = "lintcode"
T = "lint"
output:
true

"""
class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        if not t:
            return True
        
        si, ti = 0, 0
        
        while si < len(s):
            if ti == len(t):
                #found 
                break
            
            if s[si] == t[ti]:
                si += 1 
                ti += 1 
            else:
                si += 1 
                
        return ti == len(t)