# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: (x.start, x.end))
        result = []
        for interval in intervals:
            if not result or interval.start > result[-1].end:
                result.append(interval)
            else:
                result[-1].end = max(interval.end, result[-1].end)

        return result
