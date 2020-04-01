class Solution:
    def subarraySum(self, nums, k: int):
        curr, ans = 0, 0
        mp = {0:1}
        for i in range(len(nums)):
            curr += nums[i] 
            ans += mp.get(curr-k, 0) 
            mp[curr] = mp.get(curr, 0) + 1 
        return ans