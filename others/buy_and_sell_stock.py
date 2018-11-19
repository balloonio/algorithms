# buy and sell stock 1
import math


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        sliding_min = math.inf
        max_profit = -math.inf
        for num in prices:
            max_profit = max(max_profit, num - sliding_min)
            sliding_min = min(sliding_min, num)
        return 0 if max_profit < 0 else max_profit


# buy and sell stock 2
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        cost = prices[0]
        profit = 0
        for p in prices:
            profit += (p - cost) if (p - cost) > 0 else 0
            cost = p
        return profit


# buy and sell stock 3
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        """
        Since we can make two transactions, we have 5 status
        0 - Before the first buy
        1 - Holding the first buy
        2 - Sold the first buy and before the second buy
        3 - Holding the the second buy
        4 - Sold the second buy
        
        Define a DP array f[i][j] to indicate
        The max possible profit at day i (prices[i]) with current holding status j
        """

        n = len(prices)
        f = [[None] * 5 for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):

            # no holding before first buy, no profit
            f[i][0] = 0

            # holding after the first buy
            stay_hold = (
                None
                if i < 2 or f[i - 1][1] is None
                else f[i - 1][1] + prices[i - 1] - prices[i - 2]
            )
            new_buy = f[i - 1][0]
            if stay_hold is None and new_buy is None:
                f[i][1] = None
            elif stay_hold is None or new_buy is None:
                f[i][1] = stay_hold if stay_hold is not None else new_buy
            else:
                f[i][1] = max(stay_hold, new_buy)

            # flat after the first sell
            stay_flat = f[i - 1][2]
            new_sell = (
                None
                if i < 2 or f[i - 1][1] is None
                else f[i - 1][1] + prices[i - 1] - prices[i - 2]
            )
            if stay_flat is None and new_sell is None:
                f[i][2] = None
            elif stay_flat is None or new_sell is None:
                f[i][2] = stay_flat if stay_flat is not None else new_sell
            else:
                f[i][2] = max(stay_flat, new_sell)

            # holding after the second buy
            stay_hold = (
                None
                if i < 2 or f[i - 1][3] is None
                else f[i - 1][3] + prices[i - 1] - prices[i - 2]
            )
            new_buy = f[i - 1][2]
            if stay_hold is None and new_buy is None:
                f[i][3] = None
            elif stay_hold is None or new_buy is None:
                f[i][3] = stay_hold if stay_hold is not None else new_buy
            else:
                f[i][3] = max(stay_hold, new_buy)

            # flat after the second sell
            stay_flat = f[i - 1][4]
            new_sell = (
                None
                if i < 2 or f[i - 1][3] is None
                else f[i - 1][3] + prices[i - 1] - prices[i - 2]
            )
            if stay_flat is None and new_sell is None:
                f[i][4] = None
            elif stay_flat is None or new_sell is None:
                f[i][4] = stay_flat if stay_flat is not None else new_sell
            else:
                f[i][4] = max(stay_flat, new_sell)

        profit = 0
        profit = max(profit, f[-1][2]) if f[-1][2] is not None else profit
        profit = max(profit, f[-1][4]) if f[-1][4] is not None else profit
        return profit


# buy and sell stock 4
class Solution:
    def maxProfit(self, K, prices):
        if not prices:
            return 0

        n = len(prices)
        if K > n / 2:
            return self.buy_and_sell_i(prices)

        """
        readable version, not optimized for memory
        # f[i][j] stands for max profit for the first i days with the last day ending in j state
        f = [ [-math.inf] * (2*K+1) for _ in range(n+1) ]
        f[0][0] = 0
        
        for i in range(1, n+1):
            f[i][0] = 0
            for j in range(1, 2*K+1):
                # holding
                if j % 2 == 1:
                    stay_hold = f[i-1][j] + prices[i-1] - prices[i-2] if i >= 2 else -math.inf
                    new_buy = f[i-1][j-1]
                    f[i][j] = max(stay_hold, new_buy)
                else:
                    stay_flat = f[i-1][j]
                    new_sell = f[i-1][j-1] + prices[i-1] - prices[i-2] if i >= 2 else -math.inf 
                    f[i][j] = max(stay_flat, new_sell)
        
        profit = 0
        for j, local_profit in enumerate(f[-1]):
            if j % 2 == 0:
                profit = max(profit, local_profit)
        return profit
        """
        f = [-math.inf] * (2 * K + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in reversed(range(1, 2 * K + 1)):
                if j % 2 == 0:  # flat
                    stay_flat = f[j]
                    new_sell = (
                        f[j - 1] + prices[i - 1] - prices[i - 2]
                        if i >= 2
                        else -math.inf
                    )
                    f[j] = max(stay_flat, new_sell)
                else:  # holding
                    stay_hold = (
                        f[j] + prices[i - 1] - prices[i - 2] if i >= 2 else -math.inf
                    )
                    new_buy = f[j - 1]
                    f[j] = max(stay_hold, new_buy)
        profit = 0
        for j in range(2 * K + 1):
            if j % 2 == 0:
                profit = max(profit, f[j])
        return profit

    def buy_and_sell_i(self, prices):
        n = len(prices)

        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


sol = Solution()
prices = [2, 1, 2, 0, 1]
print(sol.maxProfit(prices))
