"""
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution:
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if len(s) <= n or n == 1:
            return s

        # first row char indices in original s
        # 0, (n*2-2), (n*2-2)*2, ...
        # last row char indices in original s
        # n-1, n-1 + (n*2-2), n-1 + (n*2-2)*2, ...
        # rows in the middle, row 1 to row n-2
        # e.g. row 1: 1, 1+(n*2-2), 1+(n*2-2)*2, ... plus each of them has a +(n*2-2)-row*2 item after
        slen = len(s)
        result = ""
        for row in range(n):
            gap1 = (n*2-2)
            gap2 = (n*2-2)-row*2
            rowi = row 
            while rowi < slen:
                result += s[rowi]
                result += s[rowi + gap2] if row != 0 and row != n-1 and rowi + gap2 < slen else ""
                rowi += gap1
        return result
