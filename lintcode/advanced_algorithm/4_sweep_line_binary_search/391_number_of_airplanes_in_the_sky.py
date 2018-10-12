"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0

        events = []  # (timestamp, True for taking off/ False for landing)
        for interval in airplanes:
            take_off = (interval.start, True)
            land = (interval.end, False)
            events += [take_off, land]

        events.sort()

        result = 0
        in_air = 0
        for (time, take_off) in events:
            in_air += 1 if take_off else -1
            result = max(result, in_air)

        return result
