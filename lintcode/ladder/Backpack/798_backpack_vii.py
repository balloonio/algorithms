class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    def backPackVII(self, money, prices, weight, amounts):
        # write your code here
        if not prices or not weight or not amounts:
            return 0
        
        n = sum(amounts)
        f = [ [0]*(money+1) for _ in range(n+1) ]
        
        for i in range(money+1):
            f[0][i] = 0
            
        result = 0
        for i in range(1, n+1):
            p, w = self.get_ith_item(i, prices, weight, amounts)
            for j in range(money+1):
                f[i][j] = max(f[i][j], f[i-1][j])
                f[i][j] = max(f[i][j], f[i-1][j-p] + w) if j-p >= 0 else f[i][j]
                
                if i == n:
                    result = max(result, f[i][j])
        
        return result
        
    def get_ith_item(self, ith, prices, weight, amounts):
        if ith == 0:
            return 0, 0
        
        for i, amount in enumerate(amounts):
            ith -= amount
            if ith <= 0:
                return prices[i], weight[i]