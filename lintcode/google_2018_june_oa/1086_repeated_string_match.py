""" 
Description
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

The length of A and B will be between 1 and 10000.

Have you met this question in a real interview?  
Example
with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
"""


class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """

    def repeatedStringMatch(self, A, B):
        # write your code here
        if not B:
            return True
        if not A:
            return False

        adict, bdict = collections.defaultdict(int), collections.defaultdict(int)

        for c in A:
            adict[c] += 1

        for c in B:
            bdict[c] += 1

        rep_need = 0
        for char, freq in bdict.items():
            if char not in adict:
                return -1
            afreq = adict[char]
            rep_need = max(rep_need, math.ceil(freq / afreq))

        newa = A * rep_need
        if B in newa:
            return rep_need

        newa = A * (rep_need + 1)
        if B in newa:
            return rep_need + 1

        return -1
