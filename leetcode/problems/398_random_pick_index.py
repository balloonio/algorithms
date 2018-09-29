class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for idx, num in enumerate(nums):
            nums[idx] = (num, idx)
        nums.sort()
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # find the indices of the first and the last elemnts with num == target
        first = self.find_first_idx(target)
        last = self.find_first_idx(target, foundLast=True)
        # assert first, last != -1
        picked = random.choice(self.nums[first : last + 1])
        return picked[1]

    def find_first_idx(self, target, foundLast=False):
        start, end = 0, len(self.nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if not foundLast:
                if self.nums[mid][0] < target:
                    start = mid
                else:
                    end = mid
            else:
                if self.nums[mid][0] <= target:
                    start = mid
                else:
                    end = mid
        if foundLast:
            if self.nums[end][0] == target:
                return end
            elif self.nums[start][0] == target:
                return start
        else:
            if self.nums[start][0] == target:
                return start
            elif self.nums[end][0] == target:
                return end
        return -1  # not in the array
