class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        
        for end in range(len(nums)):
            if nums[end]!=0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
        
        return nums