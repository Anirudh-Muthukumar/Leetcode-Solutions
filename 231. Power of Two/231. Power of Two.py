class Solution:
    def isPowerOfTwo(self, n):
        
        while n > 1:
            if n%2==0:
                n = n// 2
            else:
                return False
        
        return n==1