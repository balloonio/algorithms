class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False

        # f[i] = given i coins from values starting from the right side,
        # how greater diff the first player can get compared to the other player
        values.reverse()
        n = len(values)
        f = [-math.inf] * (n + 1)
        f[0] = 0

        for i in range(1, n + 1):
            # take 1 coin
            f[i] = max(values[i - 1] - f[i - 1], f[i])
            # or, take 2 coin
            f[i] = (
                max(values[i - 1] + values[i - 2] - f[i - 2], f[i]) if i >= 2 else f[i]
            )

        return f[-1] > 0
