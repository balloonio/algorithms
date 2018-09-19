class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        carry = 0
        result = ""

        alen, blen = len(a), len(b)
        maxlen = max(alen, blen)
        a = a[::-1]
        b = b[::-1]

        for i in range(maxlen):
            adigit = 0 if i >= alen else int(a[i])
            bdigit = 0 if i >= blen else int(b[i])
            rdigit = adigit ^ bdigit ^ carry
            carry = (adigit + bdigit + carry - rdigit) // 2
            result += str(rdigit)

        if carry:
            result += str(carry)
        result = result[::-1]
        return result
