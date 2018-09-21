class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 1

        # f[i] = how many ways to decode the first i characters
        slen = len(s)
        f = [0] * (slen + 1)
        f[0] = 1

        for i in range(1, slen + 1):
            # take 1 digit
            one_digit = s[i - 1]
            one_way = self.get_decode_ways(one_digit)
            f[i] += f[i - 1] * one_way
            # take 2 digits
            if i - 2 >= 0:
                two_digit = s[i - 2 : i]
                two_way = self.get_decode_ways(two_digit)
                f[i] += f[i - 2] * two_way
            f[i] %= 10 ** 9 + 7

        return f[slen] % (10 ** 9 + 7)

    def get_decode_ways(self, s):
        if len(s) == 1:
            if s == "0":
                return 0
            elif s == "*":
                return 9
            else:
                return 1

        if s[0] == "*" and s[1] == "*":
            return 15
        if s[0] == "*":
            return 1 if int(s[1]) >= 7 and int(s[1]) <= 9 else 2
        if s[1] == "*":
            if s[0] == "1":
                return 9
            if s[0] == "2":
                return 6
            return 0

        val = int(s)
        return 1 if val >= 10 and val <= 26 else 0


# be careful, '*' only counts for 1-9, not 0
