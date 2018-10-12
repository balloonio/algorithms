class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        if not nums or not k:
            return 0

        min_num, max_num = math.inf, -math.inf
        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        start, end = min_num, max_num
        while start + 1e-5 < end:
            mid = (start + end) / 2
            if self.is_average_satisfied(mid, nums, k):
                start = mid
            else:
                end = mid

        return start

    def is_average_satisfied(self, avg, nums, k):
        diff = [x - avg for x in nums]
        min_sum = 0
        left_sum = 0
        right_sum = sum(diff[:k])
        if right_sum - min_sum >= 0:
            return True

        for i in range(k, len(diff)):
            right_sum += diff[i]
            left_sum = left_sum + diff[i - k]
            min_sum = min(min_sum, left_sum)
            if right_sum - min_sum >= 0:
                return True

        return False
