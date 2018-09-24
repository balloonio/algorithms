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

        # f[i][j] = min dist between s[:i] and t[:t]
        slen, tlen = len(s), len(t)
        f = [[0] * (tlen + 1) for _ in range(slen + 1)]

        for i in range(slen + 1):
            for j in range(tlen + 1):
                if i == 0 and j == 0:
                    continue
                f[i][j] = math.inf
                # same char, same as before
                if i - 1 >= 0 and j - 1 >= 0 and s[i - 1] == t[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                # different char
                if i - 1 >= 0 and j - 1 >= 0 and s[i - 1] != t[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
                # by s[:i-1] adding 1 char to meet t[:j]
                if i - 1 >= 0:
                    f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                # by t[:j-1] adding 1 char to meet s[:i]
                if j - 1 >= 0:
                    f[i][j] = min(f[i][j], f[i][j - 1] + 1)

        return f[slen][tlen] == 1


# This DP solution is TLE
# This problem can be done in linear time
