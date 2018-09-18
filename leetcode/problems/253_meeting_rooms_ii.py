# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        events = []
        for interval in intervals:
            start, end = interval.start, interval.end
            events += [(start, 1)]
            events += [(end, 0)]
        events.sort()

        max_meeting = 0
        curr_meeting = 0
        for event in events:
            time, is_start = event
            if is_start:
                curr_meeting += 1
            else:
                curr_meeting -= 1
            max_meeting = max(max_meeting, curr_meeting)
        return max_meeting
