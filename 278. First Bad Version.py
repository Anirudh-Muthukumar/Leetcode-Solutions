'''
Time complexity : O(log n)
Space complexity: O(1)
'''

def isBadVersion(version):
    ''' Inbuilt '''
    pass 

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        
        while lo<hi:
            mid = (lo + hi) // 2
            
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1 
            
            elif not isBadVersion(mid) and not isBadVersion(mid+1):
                lo = mid
            
            else:
                hi = mid
        
        return lo