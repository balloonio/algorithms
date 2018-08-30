class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0 
        
        n = len(costs)
        COLORS = 3
        # f[i][j] - the lowest cost to build the first i houses under the condition that last house is j colored
        f = [ [0]*COLORS for i in range(n+1) ]
        
        # cost to build first 0 houses is 0
        for i in range(COLORS):
            f[0][i] = 0
            
        # paint from first 1 house to first n houses
        for i in range(1, n+1):
            for j in range(COLORS):
                f[i][j] = math.inf
                for k in range(COLORS):
                    f[i][j] = min(f[i-1][k], f[i][j]) if j != k else f[i][j]
                f[i][j] += costs[i-1][j]
        
        return min(f[-1])