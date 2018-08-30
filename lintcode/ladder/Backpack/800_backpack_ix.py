class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """
    def backpackIX(self, n, prices, probability):
        # write your code here
        dp = [1.0 for x in range(n + 1)]
        for i in range(len(probability)):
            probability[i] = 1 - probability[i]
           
        for i in range(len(probability)):  
            j = n
            while j >= prices[i]:  
               dp[j] = min(dp[j], dp[j-prices[i]] * probability[i])
               j = j - 1
        return 1 - dp[n]