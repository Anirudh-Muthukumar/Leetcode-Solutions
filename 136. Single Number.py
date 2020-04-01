'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
        
        return res