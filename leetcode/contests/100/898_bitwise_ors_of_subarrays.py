class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return []

        max_or = 0
        for num in A:
            max_or |= num

        result = set()
        n = len(A)
        for start in range(n):
            or_val = 0
            for end in range(start, n):
                or_val |= A[end]
                result.add(or_val)
                if or_val == max_or:
                    break

        return len(result)


# must read - https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165933/Python-Dynamic-programming-solution-with-indepth-explanation-of-intuition.
