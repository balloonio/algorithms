# 1. my naive sorting solution NlogN
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        occurance = 0
        last = None
        removed = 0
        for i, num in enumerate(nums):
            if last is None or num != last:
                occurance = 1
                last = num
                continue
            occurance += 1
            if occurance > 2:
                nums[i] = math.inf
                removed += 1
                occurance -= 1

        nums.sort()
        return len(nums) - removed


# 2. Saw a 1 ptr O(N) solution on LeetCode
#    Wrote in my own non-genius readable language


class Solution:  # noqa: F811
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        idx_to_place = 0
        placed_cnt = 0
        last_num = None
        for num in nums:
            if last_num is None or num != last_num:
                placed_cnt = 0
            if placed_cnt < 2:
                nums[idx_to_place] = num
                idx_to_place += 1
                placed_cnt += 1
            last_num = num

        return idx_to_place


"""
in place, but you can modify
The second solution is very important, as it is a typical One Pointer Assignment
solution that I saw before in similar questions. (Although I didn't come up with
one this time... but at least I learned something from others)
"""
