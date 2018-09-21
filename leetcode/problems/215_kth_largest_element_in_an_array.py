class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        return self.quick_select(nums, k, 0, len(nums) - 1)

    def quick_select(self, nums, k, start, end):
        if start == end:
            return nums[start]

        mid = (start + end) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k - 1 <= right:
            return self.quick_select(nums, k, start, right)
        elif k - 1 >= left:
            return self.quick_select(nums, k, left, end)
        return nums[right + 1]
