'''

Since given array is circular the robber cannot steal house[0] and house[n-1] simultaneously. 
Compute the maximum sum subsequence with no adjacent elements for both cases separately and 
return the maximum. 

Time complexity : O(n)
Space complexity: O(n)

'''

def rob(nums) -> int:
        
        def maximumSum(nums, n):
            nonlocal lookup
            
            if n<0:
                return 0
            
            key = str(nums) + '|' + str(n)
            
            if key not in lookup:
                # include current element and recur for n-2
                include = nums[n] + maximumSum(nums, n-2)
                
                # exclude current element and recur for n-1
                exclude = maximumSum(nums, n-1)
                
                lookup[key] = max(include, exclude)
            
            return lookup[key]
    
        lookup = {}
        
        n = len(nums)
        
        if n==0:
            return 0
        
        if 1<=n<=3:
            return max(nums)
        
        # exclude first house
        first_house = maximumSum(nums[1:], n-2)

        # exclude last house
        last_house = maximumSum(nums[:-1], n-2)

        return max(first_house, last_house)


if __name__ == '__main__':
    
    arr = [1,2,3,4,5,6] 

    print("\nAnswer = %d\n" % rob(arr))
