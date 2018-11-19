import math


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        if not A and not B:
            raise ValueError
        if not A or not B:
            return self.get_median(A) if A else self.get_median(B)

        """
        for array A, we binary search to pick a number x (0 <= x <= len(A))
        so that the leftmost x numbers from A and the leftmost y numbers from B 
        are the smaller half of the numbers in the total merged list (if merged)
        """
        size = len(A) + len(B)
        half_size = (size + 1) // 2
        start, end = 0, len(A)

        while start + 1 < end:
            x = (start + end) // 2
            rc = self.is_partition_good_for_x_picked(A, B, half_size, x)
            if rc == "XGOOD":
                return self.get_median_for_x(A, B, half_size, x)
            elif rc == "XTOOLARGE":
                end = x
            else:
                start = x

        if self.is_partition_good_for_x_picked(A, B, half_size, start) == "XGOOD":
            return self.get_median_for_x(A, B, half_size, start)

        return self.get_median_for_x(A, B, half_size, end)

    def is_partition_good_for_x_picked(self, A, B, half_size, x):
        y = half_size - x

        if y < len(B) and A[x - 1] > B[y]:
            return "XTOOLARGE"
        if x < len(A) and B[y - 1] > A[x]:
            return "XTOOSMALL"
        return "XGOOD"

    def get_median_for_x(self, A, B, half_size, x):
        y = half_size - x
        left, right = -math.inf, math.inf

        if x - 1 >= 0:
            left = max(left, A[x - 1])
        if y - 1 >= 0:
            left = max(left, B[y - 1])
        if x < len(A):
            right = min(right, A[x])
        if y < len(B):
            right = min(right, B[y])

        size = len(A) + len(B)
        if size % 2 == 1:
            return left
        return (left + right) / 2

    def get_median(self, array):
        size = len(array)

        if size % 2 == 1:
            return array[size // 2]

        return (array[(size - 1) // 2] + array[size // 2]) / 2
