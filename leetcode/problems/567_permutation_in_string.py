class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)

        if not s2 or len2 < len1:
            return False
        if not s1:
            return True

        # compare to permutation of s1, current window is missing(-) or having too much(+) of char
        window_diff = collections.defaultdict(int)
        for c in s1:
            window_diff[c] -= 1

        for i in range(len1):
            char = s2[i]
            window_diff[char] += 1
            if window_diff[char] == 0:
                window_diff.pop(char)

        if len(window_diff) == 0:
            return True

        for i in range(len1, len2):
            char = s2[i]
            char2rm = s2[i - len1]
            window_diff[char] += 1
            window_diff[char2rm] -= 1
            if window_diff[char] == 0:
                window_diff.pop(char)
            if window_diff[char2rm] == 0:
                window_diff.pop(char2rm)
            if len(window_diff) == 0:
                return True

        return False
