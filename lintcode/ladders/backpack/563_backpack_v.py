class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        # write your code here
        if not nums:
            return 0

        n = len(nums)

        # f[i][j] = number of ways to fill backpack with first i items and target j
        f = [0] * (target + 1)

        for i in xrange(target + 1):
            f[i] = 0
        f[0] = 1

        for i in xrange(1, n + 1):
            for j in reversed(range(target + 1)):
                f[j] = f[j] + (f[j - nums[i - 1]] if j - nums[i - 1] >= 0 else 0)

        return f[-1]
