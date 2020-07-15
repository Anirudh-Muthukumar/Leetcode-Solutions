class Solution:
    def maxProfit(self, K, prices):
        n = len(prices)    
        if n==0:
            return 0
        
        if K >= n>>1:
            res = 0
            for i in range(1, n):
                res += (prices[i] - prices[i-1]) if prices[i] > prices[i-1] else 0
            return res
            

        dp = [0 for _ in range(K+1)]
        price_j = [prices[0] for _ in range(K+1)]
        
        for i in range(1, n):
            for k in range(1, K+1):
                price_j[k] = min(price_j[k], prices[i] - dp[k-1])
                dp[k] = max(dp[k], prices[i] - price_j[k])
                
        
        return dp[K]

