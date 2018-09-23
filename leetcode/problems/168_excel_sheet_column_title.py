class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        result = ""
        while n:
            remain = n % 26
            remain = 26 if remain == 0 else remain
            digit = self.digit_dec_to_26(remain)
            result = digit + result
            n = (n - remain) // 26
        return result

    def digit_dec_to_26(self, n):
        if n <= 0 or n > 26:
            return None
        return chr(ord("A") + n - 1)


"""
This is slightly different from digit conversion
L12 if n is 26, the output is still single digit and show as 'Z' not 'BA'
Therefore, pass in 1-26 into the digit conversion
L15 remove the single digit that we already counted, and then do the division
"""
