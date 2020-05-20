def findUnsortedSubarray(self, nums):
        
        n = len(nums)
        
        if n<=1:
            return 0

        lo = 0
        hi = len(nums)-1
        
        # find the position of lo
        while lo<n and nums[lo]==min(nums[lo:]):
            lo += 1
        
        if lo==n:
            return 0
        

        # find the position of hi
        while hi>=0 and nums[hi]==max(nums[:hi+1]):
            hi -= 1

        
        if hi==len(nums)-1 and lo==0:
            return n
        
        return hi-lo+1

