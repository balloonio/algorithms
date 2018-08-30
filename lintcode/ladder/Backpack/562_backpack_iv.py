class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)
        f = [ [0]*(target+1) for _ in range(n+1) ]
        f[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(target+1):
                f[i][j] += f[i-1][j]
                f[i][j] += f[i][j-nums[i-1]] if j-nums[i-1] >= 0 else 0
        
        return f[-1][-1]