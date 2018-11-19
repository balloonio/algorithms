class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False

        slen, plen = len(s), len(p)

        # a-z current char must match, before and before must match
        # ? before must match
        # * 1. if this * was matching before, then this * can match 1 more char
        #   2. if the stuff before this * is matching the s before, then match
        #   3. if the stuff before this * matches the current s, then match

        # f[i][j] = p[:i] matches s[:j] or not
        f = [[False] * (slen + 1) for _ in range(plen + 1)]
        f[0][0] = True

        for i in range(1, plen + 1):
            for j in range(slen + 1):
                if j == 0:
                    f[i][j] = p[i - 1] == "*" and f[i - 1][j]
                    continue
                char = p[i - 1]
                if ord(char) >= ord("a") and ord(char) <= ord("z"):
                    f[i][j] = f[i - 1][j - 1] and p[i - 1] == s[j - 1]
                elif char == "?":
                    f[i][j] = f[i - 1][j - 1]
                elif char == "*":
                    f[i][j] = f[i - 1][j - 1] or f[i][j - 1] or f[i - 1][j]
        # print(f)
        return f[plen][slen]


# L35 bug f[i][j] = f[i-1][j-1] or f[i][j-1]

"""
memo search
"""
class Solution:
    def __init__(self):
        self.memo = {}

    def isMatchList(self, s, si, p, pi):
        # print(s, si, p, pi)
        if (si, pi) in self.memo:
            return self.memo[si, pi]

        if si == len(s):
            self.memo[si, pi] = p[pi:].count("*") == len(p) - pi
            return self.memo[si, pi]
        if pi == len(p):
            self.memo[si, pi] = not s[si:]
            return self.memo[si, pi]

        if p[pi] == "?" or p[pi] == s[si]:
            self.memo[si, pi] = self.isMatchList(s, si + 1, p, pi + 1)
        elif p[pi] == "*":
            self.memo[si, pi] = self.isMatchList(s, si + 1, p, pi) or self.isMatchList(s, si, p, pi + 1)
        else:
            self.memo[si, pi] = False
        return self.memo[si, pi]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = list(s)
        p = list(p)
        result = self.isMatchList(s, 0, p, 0)
        # print(self.memo)
        return result