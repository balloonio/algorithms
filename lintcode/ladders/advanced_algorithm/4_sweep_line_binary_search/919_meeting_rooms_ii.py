"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0

        events = []
        for interval in intervals:
            events += [(interval.start, True)]
            events += [(interval.end, False)]

        events.sort()

        max_meeting = 0
        meeting_same_time = 0
        for (time, is_start) in events:
            meeting_same_time += 1 if is_start else -1
            max_meeting = max(max_meeting, meeting_same_time)

        return max_meeting
