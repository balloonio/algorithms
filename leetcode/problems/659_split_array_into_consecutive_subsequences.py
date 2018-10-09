import heapq
class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) < 3:
            return False
        """
        visualize the numbers, its like a bunch of tetris with len >= 3 dropping down
        when the thickness increase, it means a new combination is dropped on top
        all we need to make sure is the length greater or equal to 3
        """
        currleft = []
        for num, rep in enumerate(self.get_number_rep(nums)):
            if rep == len(currleft):
                continue
            if rep < len(currleft):
                delta = len(currleft) - rep
                for _ in range(delta):
                    left = heapq.heappop(currleft)
                    if num - left < 3:
                        return False
                continue
            delta = rep - len(currleft)
            for _ in range(delta):
                heapq.heappush(currleft, num)
        return True


    def get_number_rep(self, nums):
        maxnum = max(nums)
        count = [0] * (maxnum + 1)
        for num in nums:
            count[num] += 1
        count.append(0)
        return count
