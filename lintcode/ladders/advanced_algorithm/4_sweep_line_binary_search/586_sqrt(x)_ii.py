class Solution:
    """
    @param x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        if not x:
            return 0
        if x >= 1:
            start, end = 1, x
        else:
            start, end = 0, 1

        while start + 1e-10 < end:
            mid = (start + end) / 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid

        return start
