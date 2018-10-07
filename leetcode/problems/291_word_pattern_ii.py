class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        return self.dfs(pattern, 0, str, 0, {}, {})

    def dfs(self, p, pidx, s, sidx, p2s, s2p):
        if pidx == len(p) and sidx == len(s):
            return True
        if pidx == len(p) or sidx == len(s):
            return False
        # try to match p[pidx] against different substr in s, from s[sidx] to s[sidx:]
        matchp = p[pidx]
        for i in range(sidx, len(s)):
            if len(s) - i < len(p) - pidx:
                break
            matchs = s[sidx : i + 1]
            if matchs in s2p and s2p[matchs] != matchp:
                continue
            if matchp in p2s and p2s[matchp] != matchs:
                continue

            # here either both match not in map, or both in map and valid
            is_new_mappinng = matchs not in s2p and matchp not in p2s
            if is_new_mappinng:
                s2p[matchs], p2s[matchp] = matchp, matchs

            if self.dfs(p, pidx + 1, s, i + 1, p2s, s2p):
                return True

            if is_new_mappinng:
                s2p.pop(matchs)
                p2s.pop(matchp)
        return False


"""
L19 L20 gives huge performance improvement by pruning
"""
