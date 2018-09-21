class ParStr:
    def __init__(self):
        self.string = ""
        self.left = 0
        self.right = 0
        self.other = 0

    def push(self, char):
        self.string += char
        if char == "(":
            self.left += 1
        elif char == ")":
            self.right += 1
        else:
            self.other += 1

    def pop(self):
        char = self.string[-1]
        if char == "(":
            self.left -= 1
        elif char == ")":
            self.right -= 1
        else:
            self.other -= 1
        self.string = self.string[:-1]

    def valid(self):
        return self.left >= self.right

    def closed(self):
        return self.left == self.right


class Solution:
    def __init__(self):
        self.max_len = 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]

        result = [""]
        ps = ParStr()
        self.helper(s, 0, ps, result)
        return result

    def helper(self, s, start, ps, result):
        if ps.closed() and len(ps.string) >= self.max_len:
            if len(ps.string) > self.max_len:
                result.clear()
                self.max_len = len(ps.string)
            result.append(ps.string)

        for picked in range(start, len(s)):
            if picked != start and s[picked] == s[picked - 1]:
                continue
            ps.push(s[picked])
            if not ps.valid():
                ps.pop()
                continue
            self.helper(s, picked + 1, ps, result)
            ps.pop()
        return


# L46 - L50 has to be in every level, not just the last level
# because this is similar to subset problem, not permutation or combination
# also L53 L54 to remove duplicate
