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
