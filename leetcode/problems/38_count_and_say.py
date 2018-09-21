class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        result = "1"
        for i in range(1, n):
            result = self.say(result)

        return result

    def say(self, last):
        count = 1
        result = ""
        for i, c in enumerate(last):
            if i == 0:
                continue
            if last[i] == last[i - 1]:
                count += 1
            else:
                result += str(count) + last[i - 1]
                count = 1
        result += str(count) + c
        return result
