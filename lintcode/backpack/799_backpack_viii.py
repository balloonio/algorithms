class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """

    def backPackVIII(self, target, value, amount):
        # write your code here
        if not value or not amount:
            return False

        n = len(value)
        f = [[False] * (target + 1) for _ in range(n + 1)]
        used_coin = [0] * (target + 1)

        f[0][0] = True

        result = 0
        for i in range(1, n + 1):
            for j in range(target + 1):
                used_coin[j] = 0
                if f[i - 1][j]:
                    f[i][j] = True
                elif j - value[i - 1] >= 0 and f[i][j - value[i - 1]]:
                    f[i][j] = (
                        True if used_coin[j - value[i - 1]] < amount[i - 1] else False
                    )
                    used_coin[j] = used_coin[j - value[i - 1]] + 1

                if i == n:
                    result += 1 if j != 0 and f[i][j] else 0

        return result
