class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        # write your code here
        if not coins:
            return -1

        f = [-1] * (amount + 1)
        f[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and f[i - coin] != -1:
                    f[i] = (
                        f[i - coin] + 1 if (f[i] == -1) else min(f[i], f[i - coin] + 1)
                    )

        return f[-1]
