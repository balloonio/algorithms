class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if not citations:
            return 0

        max_cit = max(citations)
        cit2cnt = [0] * (max_cit + 1)
        for c in citations:
            cit2cnt[c] += 1

        sorted_cit = []
        for cit, count in enumerate(cit2cnt):
            sorted_cit.extend([cit] * count)

        sorted_cit.reverse()
        n = len(sorted_cit)
        for i in range(n):
            h = i + 1
            this_cit = sorted_cit[i]
            next_cit = sorted_cit[i + 1] if i + 1 < n else None
            # this citation is the last citation, h has to be n
            if next_cit is None:
                return n if this_cit >= n else 0
            if this_cit >= h and next_cit <= h:
                return h
        return 0


# L28 - still need to check if this citations satisfy the definition because there
# might be the case with one citation only [0]
