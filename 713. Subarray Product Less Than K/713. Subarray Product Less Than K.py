class Solution:
    def numSubarrayProductLessThanK(self, nums, k):

        if k<=1:
            return 0
        
        ans = 0
        lo = 0
        prod = 1
        
        for hi, num in enumerate(nums):
            prod *= num
            
            while prod>=k:
                prod = prod//nums[lo]
                lo += 1
            
            ans += (hi - lo + 1)
        
        return ans