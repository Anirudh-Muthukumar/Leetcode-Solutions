def rob(nums) -> int:
    
    # maximum sum of subsequence without adjacent elements 
    
    def maximumSum(nums, n, lookup):
        
        if n<0:
            return 0
        
        key = str(nums) + '|' + str(n)
        
        if key not in lookup:
            
            # include current element and recur for n-2
            include = nums[n] + maximumSum(nums, n-2, lookup)
            
            # exclude current element and recur for n-1
            exclude = maximumSum(nums, n-1, lookup)
            
            lookup[key] = max(include, exclude)
        
        return lookup[key]
    
    return maximumSum(nums, len(nums)-1, {})

if __name__ == '__main__':

    arr = [2,7,9,3,1] # test case

    print("Answer = ", rob(arr))