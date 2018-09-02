class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        
        reachable, index = 0, 0
        while index <= reachable and index < len(A):
            if index + A[index] > reachable:
                reachable = A[index] + index
            index += 1
        
        return reachable >= len(A) - 1