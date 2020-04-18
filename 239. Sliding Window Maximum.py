
def maxSlidingWindow(nums, k):

    if k==1:
        return nums

    # max_so_far array
    left_max = []
    max_so_far = -float('inf')
    for num in nums:
        max_so_far = max(max_so_far, num)
        left_max.append(max_so_far)
    
    
    # maximum in blocks of K 
    i = 0
    j = k 
    right_max = []
    while j<len(nums):
        right_max.extend([max(nums[i:j])] * len(nums[i:j]))
        i = j
        j += k
    
    if j>len(nums):
        right_max.extend([max(nums[i:])] * len(nums[i:]))

    window = []
    i = 0
    while i+k-1 < len(nums):
        window.append(max(right_max[i], left_max[i+k-1]))
        i+=1

    return window

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [1, -1]
# k = 1
print(maxSlidingWindow(nums, k))
        


