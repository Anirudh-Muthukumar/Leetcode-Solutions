class Solution:
    def lengthOfLIS(self, A):
        if A==[]:
            return 0
        
        dp = [0] * len(A)
        size = 0
        
        for num in A:
            # find suitable position in dp array to insert x
            i, j = 0, size
            while i!=j:       
                mid = (i+j)//2
                if dp[mid] < num:
                    i = mid+1
                else:
                    j = mid
            
            dp[i] = num
            size = max(i+1, size)
        
        return size
                