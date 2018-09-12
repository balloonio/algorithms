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
        memo = {}
        return self.helper(s, 0, p, 0, memo)

    def helper(self, s, sidx, p, pidx, memo):
        if (sidx, pidx) in memo:
            return memo[(sidx, pidx)]

        # string is exhausted
        if sidx >= len(s):
            matched = self.is_remaining_all_start(p, pidx)
            memo[(sidx, pidx)] = matched
            return matched
        # pattern is exhausted
        if pidx >= len(p):
            memo[(sidx, pidx)] = False
            return False

        # match logic
        matched = False
        pchar, schar = p[pidx], s[sidx]
        if pidx + 1 < len(p) and p[pidx+1] == '*':
            matched |= self.helper(s, sidx+1, p, pidx, memo) if pchar == schar or pchar == '.' else False
            matched |= self.helper(s, sidx, p, pidx+2, memo)
        else:
            matched |= self.helper(s, sidx+1, p, pidx+1, memo) if pchar == schar or pchar == '.' else False

        memo[(sidx, pidx)] = matched
        return matched

    def is_remaining_all_start(self, p, pidx):
        star, nonstar = 0, 0
        for c in p[pidx:]:
            star += 1 if c == '*' else 0
            nonstar += 1 if c != '*' else 0
        return star == nonstar
