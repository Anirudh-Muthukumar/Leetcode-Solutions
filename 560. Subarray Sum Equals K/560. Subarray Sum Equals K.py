'''
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def subarraySum(self, A, k):
        mp = {0: 1}
        n = len(A)
        curr = 0
        res = 0
        for i in range(n):
            curr += A[i]
            res += mp.get(curr-k, 0)
            mp[curr] = mp.get(curr, 0) + 1
        return res
        