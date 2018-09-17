class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        zero_idx, i, two_idx = 0, 0, len(nums)-1

        while i <= two_idx:
            if nums[i] == 0:
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                zero_idx += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[two_idx], nums[i] = nums[i], nums[two_idx]
                two_idx -= 1
        return

# L12 '<' would be a bug. It has too be '<=' because we need to check two_idx
