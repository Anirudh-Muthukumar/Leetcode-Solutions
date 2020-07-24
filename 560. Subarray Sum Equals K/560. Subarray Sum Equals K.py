import collections

class Solution:
    def subarraySum(self, A, k):
        mp = collections.defaultdict(int)
        mp[0] = 1
        curr = 0
        res = 0
        for x in A:
            curr += x
            res += mp.get(curr-k, 0)
            mp[curr] += 1
        return res
        