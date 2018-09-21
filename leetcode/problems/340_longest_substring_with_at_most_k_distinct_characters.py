class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0

        n = len(s)
        start, end = 0, 0
        window = collections.defaultdict(int)
        result = ""

        while start < n and end < n:
            # extend end pointer
            # so that s[start:end] is the max possible starting from s[start]
            while end < n:
                char = s[end]
                if char not in window and len(window) == k:
                    break
                window[char] += 1
                end += 1
            # record max
            result = s[start:end] if end - start > len(result) else result
            # extend start pointer until 1 distinct char is removed from window
            dist_char = len(window)
            while start < n and len(window) == dist_char:
                char = s[start]
                window[char] -= 1
                if window[char] == 0:
                    window.pop(char)
                start += 1
        return result
