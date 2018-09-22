class Solution:
    """
    @param nums:
    @param k:
    @return: return the length of subarray
    """

    def smallestLengthII(self, nums, k):
        # Write your code here
        if not nums:
            return 0

        ps = self.get_prefix_sum(nums)
        min_deque = collections.deque()
        result = None
        for i, num in enumerate(ps):
            while min_deque and ps[min_deque[-1]] >= num:
                min_deque.pop()
            while min_deque and num - ps[min_deque[0]] >= k:
                result = (
                    i - min_deque[0]
                    if result is None
                    else min(result, i - min_deque[0])
                )
                min_deque.popleft()
            min_deque.append(i)

        return result if result is not None else -1

        # ps[i] = sum(nums[:i]), ps[0] = 0

    def get_prefix_sum(self, nums):
        ps = [0]
        for num in nums:
            ps.append(ps[-1] + num)
        return ps


# 1. first thought, prefix sum for subarray sum kinda of questions
# 2. second, since there are negative numbers, the sum array sum might decrease or increase
#    therefore, we cannot use two pointers
# 3. looking for the last value that is smaller than something, maybe something like monostack or deque?
# 4. compare with Sliding Window Maximum. It seems for deque questions, deque only store valid numbers
#    e.g. either a valid max for a local sliding window, or here a number that can be used as a later subtracter
