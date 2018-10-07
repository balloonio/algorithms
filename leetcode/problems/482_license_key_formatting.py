class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        kbuf = ""
        result = ""
        for i, c in enumerate(S[::-1]):
            if c == "-":
                continue
            kbuf += c
            if len(kbuf) == K:
                result += "-" if result else ""
                result += kbuf
                kbuf = ""
        if kbuf:
            result += "-" if result else ""
            result += kbuf

        return result.upper()[::-1]


"""
The correct description of the problem is:
format the key so that any group other than the first one is strictly of length K
Whereas the first group, we dont really care about the length
And the trick here is to reverse the string to format the key so that whatever left
would be in the first group

"""
