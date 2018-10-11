class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S

        result = list(S)
        left, right = 0, len(result) - 1
        while left <= right:
            while (
                left <= right
                and result[left]
                not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
            ):
                left += 1
            while (
                left <= right
                and result[right]
                not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
            ):
                right -= 1
            if left <= right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
        return "".join(result)
