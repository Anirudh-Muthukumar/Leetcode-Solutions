'''
Time complexity : O(n * target)
Space complexity: O(target)
'''

def coinChange(self, coins: List[int], amount: int) -> int:
        
        T = [float('inf')] * (amount+1)
        T[0] = 0
        
        for total in range(1, amount+1):
            res = float('inf')
            
            for coin in coins:
                if coin<=total:
                    res = T[total-coin]
                    T[total] = min(T[total], res + 1)
        
        if T[amount]!=float('inf'):
                return T[amount]
        
        return -1
            