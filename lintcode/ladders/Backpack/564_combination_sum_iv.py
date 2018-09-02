class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0
        
        n = len(nums)
        f = [0] * (target+1)
        f[0] = 1 
        
        nums.sort()
        for i in range(1, target+1):
            for num in nums:
                if i - num < 0:
                    break
                f[i] += f[i-num]
        
        return f[target]