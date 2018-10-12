class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0

        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1

        for i in range(1, n + 1):

            # the first i - 1 characters ways of decoding
            if self.valid(s, i - 1, i - 1):
                f[i] += f[i - 1]
            if self.valid(s, i - 2, i - 1):
                f[i] += f[i - 2]

        print(f)
        return f[n]

    def valid(self, s, start, end):
        if start < 0:
            return False

        if end >= len(s):
            return False

        number = int(s[start : end + 1])
        if start == end:
            return number >= 1 and number <= 9

        return number >= 10 and number <= 26
