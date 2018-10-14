class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        stack = collections.deque()
        for char in S:
            if not stack:
                stack.append(char)
            elif stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)
