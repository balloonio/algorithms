class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        
        f = [ (0,0) for _ in nums]
        f[0] = ( nums[0], nums[0] ) # smallest product and largest product
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                f[i] = (0, 0)
                continue
            
            smallest = f[i-1][0]
            largest = f[i-1][1]
            
            if nums[i] > 0:
                f[i] = (min(smallest * nums[i], nums[i]), max(largest * nums[i], nums[i]))
            else:
                f[i] = (min(largest * nums[i], nums[i]), max(smallest * nums[i], nums[i]))
            
        max_product = -math.inf 
        for tup in f:
            largest = tup[1]
            max_product = largest if largest > max_product else max_product
        
        return max_product