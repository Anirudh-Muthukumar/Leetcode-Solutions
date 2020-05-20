class Solution:
    def maxProduct(self, nums):
        maxval, minval = 1, 1
        ans = -float('inf')
        for i in range(len(nums)):
            if nums[i]>0:
                maxval *= nums[i]
                minval = min(1, minval * nums[i])
            elif nums[i]==0: # what if all elements are either negative or 0
                maxval = 0
                minval = 1
            else: 
                # prevmax = maxval
                maxval, minval = minval * nums[i], maxval * nums[i]
            
            ans = max(maxval, ans)
            
            # maxval cannot be 0 for next iteration
            if maxval<=0:
                maxval = 1
        
        return ans