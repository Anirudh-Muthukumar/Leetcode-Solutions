'''
Time complexity : O(n)
Space complexity : O(1)
'''

def canJump(nums):
    n = len(nums)
    canReach = n-1

    for i in range(n-2, -1, -1):
        if i+nums[i] >= canReach:
            canReach = i
    
    return canReach == 0

print(canJump([3,2,1,0,4]))

