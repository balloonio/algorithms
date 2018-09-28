class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False
        if not s or not t:
            return True if abs(len(s) - len(t)) == 1 else False

        slen, tlen = len(s), len(t)
        if abs(slen - tlen) > 1:
            return False

        sidx, tidx = 0, 0
        modcnt = 0
        while sidx < slen and tidx < tlen:
            if s[sidx] == t[tidx]:
                sidx += 1
                tidx += 1
                continue
            if modcnt == 1:
                return False
            modcnt += 1
            if slen == tlen:
                sidx += 1
                tidx += 1
                continue
            if slen == tlen - 1:
                tidx += 1
            else:
                sidx += 1

        modcnt += slen - sidx + tlen - tidx

        return True if modcnt == 1 else False


# This DP solution is TLE
# This problem can be done in linear time
# L36 for the case that while loop finished but s and t are in differ length
# "a" and "ac"
