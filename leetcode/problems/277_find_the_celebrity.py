# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return -1
        if n == 1:
            return 0

        candidate = None
        for person in range(n):
            if candidate is None:
                candidate = person
                continue
            candidate_knows = knows(candidate, person)
            if candidate_knows:
                candidate = person

        for person in range(n):
            if person == candidate:
                continue
            if knows(candidate, person) or not knows(person, candidate):
                return -1
        return candidate
