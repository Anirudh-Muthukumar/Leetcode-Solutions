'''
Time complexity : O(n)
Space complexity: O(n)
'''

def findMaxLength(self, nums):
    n = len(nums)
    if n==0:
        return 0
    mp = {0: 0}
    maxlen = 0
    curr_sum = 0
    for i in range(n):
        if nums[i]==0:
            curr_sum -= 1
        else:
            curr_sum += 1
        
        if curr_sum not in mp:
            mp[curr_sum] = i + 1
        
        if maxlen < (i+1)-mp[curr_sum]:
            maxlen = (i+1)-mp[curr_sum]
    
    return maxlen