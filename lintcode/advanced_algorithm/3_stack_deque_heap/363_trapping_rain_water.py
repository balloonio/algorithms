""" 
Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
"""


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        left_max, right_max = 0, 0

        result = 0
        while left <= right:
            if left_max < right_max:
                result += left_max - heights[left] if left_max > heights[left] else 0
                left_max = max(left_max, heights[left])
                left += 1

            else:
                result += (
                    right_max - heights[right] if right_max > heights[right] else 0
                )
                right_max = max(right_max, heights[right])
                right -= 1

        return result
