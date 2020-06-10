'''
Time complexity : O(n * target)
Space complexity: O(target)
'''

class Solution:
    def coinChange(self, coins, amount):
        T = [float('inf')] * (amount+1)
        T[0] = 0
        
        for i in range(1, amount+1):
            for j in coins:
                if j<=i:
                    T[i] = min(T[i], T[i-j]+1)
        
        if T[amount] < float('inf'):
            return T[amount]
        
        return -1
            